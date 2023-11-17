from databaseConnection import cursor, get_result_from_database

# according to deliverable3 #1 #2 #3
def get_quantity_sold_categories(NTILENum):
  # query
  query = f"""
    SELECT 
      Categories.CategoriesID,
      Categories.CategoriesName, 
      SUM(Transactions.Quantity) as Quantity_Sold,
      NTILE({NTILENum}) OVER (ORDER BY SUM(Transactions.Quantity) DESC) as {NTILENum}Tile,
      ROUND(PERCENT_RANK() OVER (ORDER BY SUM(Transactions.Quantity) DESC) * 100, 2) as Percentage_Rank
    FROM 
      Transactions 
    JOIN 
      Products ON Transactions.ProductID = Products.ProductID 
    JOIN 
      Categories ON Products.CategoriesID = Categories.CategoriesID 
    GROUP BY 
      Categories.CategoriesID,
      Categories.CategoriesName
    ORDER BY 
      Quantity_Sold DESC;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# according to deliverable3 #1 #2 #3
def get_quantity_sold_products(NTILENum):
  # query
  query = f"""
    SELECT 
      Products.ProductID, 
      Products.ProductName, 
      Categories.CategoriesName, 
      SUM(Transactions.Quantity) as Quantity_Sold,
      NTILE({NTILENum}) OVER (ORDER BY SUM(Transactions.Quantity) DESC) as {NTILENum}Tile,
      ROUND(PERCENT_RANK() OVER (ORDER BY SUM(Transactions.Quantity) DESC) * 100, 2) as Percentage_Rank
    FROM 
        Transactions 
    JOIN 
        Products ON Transactions.ProductID = Products.ProductID 
    JOIN 
        Categories ON Products.CategoriesID = Categories.CategoriesID
    GROUP BY 
        Products.ProductID, 
        Products.ProductName, 
        Categories.CategoriesName 
    ORDER BY 
        Quantity_Sold DESC;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# according to deliverable3 #4
def get_quantity_sold(start_date, end_date):  
  # query
  query = f"""
    SELECT 
        Products.ProductID,
        Products.ProductName,
        Categories.CategoriesID, 
        Categories.CategoriesName,
        Suppliers.SupplierID, 
        Suppliers.SupplierName,
        MIN(Transactions.TransactionsDate) AS FirstTransactionDate, 
        MAX(Transactions.TransactionsDate) AS LastTransactionDate,
        SUM(Transactions.Quantity) as Quantity_Sold
    FROM 
        Transactions 
    JOIN 
        Products ON Transactions.ProductID = Products.ProductID 
    JOIN 
        Suppliers ON Products.SupplierID = Suppliers.SupplierID 
    JOIN 
        Categories ON Products.CategoriesID = Categories.CategoriesID
    WHERE 
        Transactions.TransactionsDate BETWEEN "{start_date}" AND "{end_date}"
    GROUP BY 
        Products.ProductID,
        Products.ProductName
    ORDER BY 
        Products.ProductID,
        Categories.CategoriesID;
    """
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# according to deliverable3 #6 #7 #8 #27
def get_profits():
  query = """
    SELECT 
      EXTRACT(YEAR FROM TransactionsDate) as Year, 
      EXTRACT(MONTH FROM TransactionsDate) as Month,
      COUNT(TransactionsID) AS TransactionCount,
      Sum(Price*Quantity) as Revenue, 
      SUM(Cost*Quantity) as cost, 
      (SUM(Price*Quantity)-SUM(Cost*Quantity)) as Profit 
    FROM 
      Products 
    JOIN 
      Transactions ON Products.ProductID=Transactions.ProductID 
    GROUP BY 
      Year,
      Month 
    ORDER BY 
      Year,
      Month;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# use UNION
def get_total_revenue():
  query = """
    SELECT
      'TotalRevenue' AS DataType,
      p.ProductID,
      p.ProductName,
      SUM(t.Quantity) AS TotalSoldQuantity,
      SUM(p.Price * t.Quantity) AS TotalRevenue
    FROM
      Transactions t
    JOIN
      Products p ON t.ProductID = p.ProductID
    GROUP BY
      p.ProductID, p.ProductName

    UNION

    SELECT
      'TotalExpenditure' AS DataType,
      p.ProductID,
      p.ProductName,
      SUM(i.Quantity) AS TotalInventory,
      SUM(p.Cost * i.Quantity) AS TotalExpenditure
    FROM
      Inventory i
    JOIN
      Products p ON i.ProductID = p.ProductID
    GROUP BY
      p.ProductID, p.ProductName
    ORDER BY
      DataType, ProductID;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# according to deliverable3 #9
def get_buyer_info():
  query = """
    SELECT 
      Transactions.BuyerID,
      Buyers.name_Firstname,
      Transactions.TransactionsDate,
      Products.ProductName,
      Transactions.Quantity,
      SUM(Transactions.Quantity) OVER (PARTITION BY Buyers.BuyerID ORDER BY Transactions.TransactionsDate) AS Cumulative_Quantity
    FROM 
      Transactions
    JOIN 
      Products ON Transactions.ProductID = Products.ProductID
    JOIN 
      Buyers ON Transactions.BuyerID = Buyers.BuyerID
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# according to deliverable3 #11
def get_product_out_of_stock():
  query = """
    SELECT
      P.ProductID,
      P.ProductName,
      S.SupplierName,
      S.ContactDetail_Phone,
      P.Cost,
      COALESCE(i.Quantity, 0) AS Quantity,
      'Not in any warehouse' AS Note
    FROM
      Products AS P
    LEFT JOIN
      Inventory AS I ON P.ProductID = I.ProductID
    LEFT JOIN
      Suppliers AS S ON P.SupplierID = S.SupplierID
    WHERE
      I.ProductID IS NULL
    ORDER BY
      P.ProductID
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# according to deliverable3 #17
def get_product_stock():
  query = """
    SELECT 
      p.ProductID,
      p.ProductName, 
      w.State,
      w.City,
      i.Quantity,
      p.Cost,
      p.Cost * i.Quantity AS ProductSubTotalCost,
      SUM(p.Cost * i.Quantity) OVER (PARTITION BY p.ProductID) AS ProductTotalCost
    FROM 
      Products p
    JOIN 
      Inventory i ON p.ProductID = i.ProductID
    JOIN 
      Warehouses w ON i.WarehouseID = w.WarehouseID
    ORDER BY
      p.ProductID,
      w.State,
      w.City;
  """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# according to deliverable3 #17
def get_stock_in_warehouse():
  query = """
    SELECT
      w.WarehouseID,
      w.State,
      w.City,
      p.ProductID,
      p.ProductName,
      i.Quantity,
      p.Cost,
      p.Cost * i.Quantity AS ProductTotalCost,
      SUM(p.Cost * i.Quantity) OVER (PARTITION BY w.WarehouseID) AS WarehouseTotalCost
    FROM
      Warehouses w
    LEFT JOIN
      Inventory i ON w.WarehouseID = i.WarehouseID
    LEFT JOIN
      Products p ON i.ProductID = p.ProductID
    ORDER BY
      w.WarehouseID,
      w.State,
      w.City,
      p.ProductID;
  """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# use WITH
def get_sales_rank():
  query = """
    WITH SalesRank AS (
      SELECT
        p.ProductID,
        p.ProductName,
        SUM(t.Quantity) AS TotalSoldQuantity,
        SUM(p.Price * t.Quantity) AS TotalSales
      FROM
        Transactions t
      JOIN
        Products p ON t.ProductID = p.ProductID
      GROUP BY
        p.ProductID, p.ProductName
    )

    SELECT
      ProductID,
      ProductName,
      TotalSoldQuantity,
      TotalSales,
      RANK() OVER (ORDER BY TotalSales DESC) AS SalesRank
    FROM
      SalesRank
    ORDER BY
      SalesRank;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# according to deliverable3 #19 #20
def get_cumulative_revenue_in_date():
  # query
  query = """
    SELECT
      Transactions.TransactionsDate,
      Products.ProductName,
      Transactions.Quantity,
      Products.Price,
      Products.Price*Transactions.Quantity as Subtotal,
      SUM(Transactions.Quantity) OVER (ORDER BY Transactions.TransactionsDate) AS Cumulative_Quantity,
      SUM(Products.Price * Transactions.Quantity) OVER (ORDER BY Transactions.TransactionsDate) AS Cumulative_Revenue
    FROM 
      Transactions
    JOIN 
      Products ON Transactions.ProductID = Products.ProductID
    ORDER BY
      Transactions.TransactionsDate;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# according to deliverable3 #21
def get_highest_inventory_value():
  query = """
    WITH ProductValueCTE AS (
      SELECT 
        p.ProductName, (p.Price * i.Quantity) AS TotalValue
      FROM 
        Products p
      JOIN 
        Inventory i ON p.ProductID = i.ProductID 
    )
    SELECT 
      ProductName, TotalValue
    FROM 
      ProductValueCTE
    ORDER BY 
      TotalValue DESC
    LIMIT 10;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# according to deliverable3 #22 use OLAP
def get_avg_subtotal_window():
  query = """
    SELECT
      Transactions.TransactionsDate,
      Products.ProductName,
      Transactions.Quantity,
      Products.Price,
      Products.Price*Transactions.Quantity as Subtotal,
      ROUND(AVG(Products.Price*Transactions.Quantity) OVER (ORDER BY Transactions.TransactionsDate ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2) AS Avg_subtotal_for_each_3_transactions
    FROM 
      Transactions
    JOIN 
      Products ON Transactions.ProductID = Products.ProductID
    ORDER BY
      Transactions.TransactionsDate;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# use WITH
def get_buyer_ranking():
  query = """
    WITH CustomerPurchase AS (
      SELECT
        t.BuyerID,
        b.name_Firstname AS CustomerName,
        COUNT(t.TransactionsID) AS TotalTransactions,
        SUM(p.Price * t.Quantity) AS TotalPurchaseAmount
      FROM
        Transactions t
      JOIN
        Buyers b ON t.BuyerID = b.BuyerID
      JOIN
        Products p ON t.ProductID = p.ProductID
      GROUP BY
        t.BuyerID, CustomerName
    )

    SELECT
      BuyerID,
      CustomerName,
      TotalTransactions,
      TotalPurchaseAmount,
      RANK() OVER (ORDER BY TotalTransactions DESC) AS CustomerRank
    FROM
      CustomerPurchase
    ORDER BY
      CustomerRank;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# according to deliverable3 #23
def get_buyer_ranking_1():
  query = """
    SELECT 
      Transactions.BuyerID,
      Buyers.name_Firstname,
      Transactions.TransactionsDate,
      Products.ProductName,
      Transactions.Quantity,
      SUM(Transactions.Quantity) OVER (PARTITION BY Buyers.BuyerID ORDER BY Transactions.TransactionsDate) AS Cumulative_Quantity
    FROM 
      Transactions
    JOIN 
      Products ON Transactions.ProductID = Products.ProductID
    JOIN 
      Buyers ON Transactions.BuyerID = Buyers.BuyerID
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# according to deliverable3 #24
def get_price_difference():
  query = """
    SELECT 
      t.ProductID, 
      TransactionsDate, 
      Price,
      LAG(Price) OVER (PARTITION BY ProductID ORDER BY TransactionsDate) AS PreviousPrice,
      Price - LAG(Price) OVER (PARTITION BY ProductID ORDER BY TransactionsDate) AS PriceChange
    FROM 
      Transactions t
    JOIN 
      Products p ON t.ProductID = p.ProductID;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# according to deliverable3 #25
def get_rank1_product_in_categories():
  query = """
    WITH RankedProducts AS (
      SELECT 
        c.CategoriesName, 
        p.ProductName, 
        p.Price,
        ROW_NUMBER() OVER (PARTITION BY c.CategoriesID ORDER BY p.Price DESC) AS `Rank`
      FROM 
        Categories c
      JOIN 
        Products p ON c.CategoriesID = p.CategoriesID
      WHERE
        p.Price > 50
    )

    SELECT 
      CategoriesName, 
      ProductName, 
      Price
    FROM 
      RankedProducts
    WHERE 
      `Rank` = 1;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

def get_state_revenue():
  query = """
    SELECT
      w.State,
      t.TransactionsDate,
      SUM(p.Price * t.Quantity) AS Revenue,
      SUM(SUM(p.Price * t.Quantity)) OVER (PARTITION BY w.State ORDER BY t.TransactionsDate) AS SubtotalRevenue,
      SUM(SUM(p.Price * t.Quantity)) OVER (PARTITION BY w.State) AS TotalRevenue
    FROM
      Inventory i
    JOIN
      Products p ON i.ProductID = p.ProductID
    JOIN
      Warehouses w ON i.WarehouseID = w.WarehouseID
    JOIN
      Transactions t ON t.ProductID = i.ProductID
    GROUP BY
      w.State, t.TransactionsDate
    ORDER BY
      w.State, t.TransactionsDate;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# according to deliverable3 #26 #15
def get_price_info_in_categories():
  query = """
    SELECT
      c.CategoriesID,
      c.CategoriesName,
      ROUND(AVG(p.Price),2) AS AvgPrice,
      MAX(p.Price) AS MaxPrice,
      MIN(p.Price) AS MinPrice,
      
      (SELECT p1.ProductName
      FROM Products p1
      WHERE p1.CategoriesID = c.CategoriesID
      ORDER BY p1.Price DESC
      LIMIT 1) AS MostExpensiveProduct,
      
      (SELECT p2.ProductName
      FROM Products p2
      WHERE p2.CategoriesID = c.CategoriesID
      ORDER BY p2.Price ASC
      LIMIT 1) AS CheapestProduct
    FROM
      Categories c
    LEFT JOIN
      Products p ON c.CategoriesID = p.CategoriesID
    GROUP BY
      c.CategoriesID,
      c.CategoriesName;
  """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# according to deliverable3 #28 #16
def get_product_info():
  query = """
    SELECT
      c.CategoriesID,
      c.CategoriesName,
      p.ProductID,
      p.ProductName,
      s.SupplierName,
      m.ManufacturerName,
      w.WarehouseID,
      i.Quantity AS InventoryQuantity
    FROM
      Products p
    JOIN
      Suppliers s ON p.SupplierID = s.SupplierID
    JOIN
      Manufacturers m ON p.ManufacturerID = m.ManufacturerID
    JOIN
      Categories c ON p.CategoriesID = c.CategoriesID
    LEFT JOIN
      Inventory i ON p.ProductID = i.ProductID
    LEFT JOIN
      Warehouses w ON i.WarehouseID = w.WarehouseID
    ORDER BY
      c.CategoriesID, p.ProductID;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data
