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

# according to deliverable3 #9
def get_most_popular_supplier():
  query = """
    SELECT 
      s.SupplierName, 
      COUNT(p.ProductID) AS ProductCount
    FROM 
      suppliers s
    LEFT JOIN 
      products p ON s.SupplierID = p.SupplierID
    GROUP BY 
      s.SupplierName
    ORDER BY 
      ProductCount DESC
    LIMIT 5;
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
        p.ProductName, 
        COALESCE(i.Quantity, 0) AS Quantity
    FROM 
        products p
    LEFT JOIN 
        inventory i ON p.ProductID = i.ProductID
    WHERE 
        COALESCE(i.Quantity, 0) = 0;
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
      i.Quantity
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
      w.State,
      w.City,
      c.CategoriesName,
      p.ProductName,
      i.Quantity
    FROM 
      Products p
    JOIN 
      Inventory i ON p.ProductID = i.ProductID
    JOIN 
      Warehouses w ON i.WarehouseID = w.WarehouseID
    JOIN 
      Categories c ON c.CategoriesID = p.CategoriesID
    ORDER BY
      w.State,
      w.City,
      c.CategoriesName
  """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# according to deliverable3 #18
def get_most_popular_categories():
  query = """
    SELECT 
      c.CategoriesName,
      SUM(t.Quantity) AS Quantity_Sold,
      SUM(p.Price*t.Quantity) AS Revenue,
      SUM(p.Cost*t.Quantity) AS Cost, 
      (SUM(p.Price*t.Quantity)-SUM(p.Cost*t.Quantity)) AS Profit 
    FROM 
      Categories c
    LEFT JOIN 
      Products p ON c.CategoriesID = p.CategoriesID
    LEFT JOIN 
      Transactions t ON p.ProductID = t.ProductID
    GROUP BY 
      c.CategoriesName
    ORDER BY 
      Quantity_Sold DESC
    LIMIT 5;
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

# according to deliverable3 #22
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

# according to deliverable3 #23
def get_buyer_ranking():
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
    SELECT 
      CategoriesName, 
      ProductName, 
      Price
    FROM (
        SELECT 
          c.CategoriesName, 
          p.ProductName, 
          p.Price,
          ROW_NUMBER() OVER (PARTITION BY c.CategoriesID ORDER BY p.Price DESC) AS `Rank`
        FROM 
          Categories c
        JOIN 
          Products p ON c.CategoriesID = p.CategoriesID
    ) ranked
    WHERE 
      `Rank` = 1;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# according to deliverable3 #26 #15
def get_categories_info():
  query = """
    SELECT 
      CategoriesName, 
      AvgPrice, 
      MaxPrice, 
      MinPrice
    FROM (      
      SELECT 
        c.CategoriesName,
        AVG(p.Price) AS AvgPrice,
        MAX(p.Price) AS MaxPrice,
        MIN(p.Price) AS MinPrice
      FROM 
        Categories c
      JOIN 
        Products p ON c.CategoriesID = p.CategoriesID
      GROUP BY 
        c.CategoriesName 
    ) Subquery
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# according to deliverable3 #26 #15
def get_avg_price_in_categories():
  query = """
    SELECT 
      c.CategoriesName, 
      AVG(p.Price) AS AvgPrice,
      MAX(p.Price) AS MaxPrice,
      MIN(p.Price) AS MinPrice
    FROM 
      Categories c
    LEFT JOIN 
      Products p ON c.CategoriesID = p.CategoriesID
    GROUP BY 
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
      t.ProductID, 
      p.ProductName, 
      s.SupplierName, 
      m.ManufacturerName
    FROM 
        Transactions t
    JOIN 
        Products p ON t.ProductID = p.ProductID
    JOIN 
        Suppliers s ON p.SupplierID = s.SupplierID
    JOIN 
        Manufacturers m ON p.ManufacturerID = m.ManufacturerID
    JOIN 
        Categories c ON p.CategoriesID = c.CategoriesID
    GROUP BY 
        t.ProductID, 
        p.ProductName, 
        s.SupplierName, 
        m.ManufacturerName;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data
