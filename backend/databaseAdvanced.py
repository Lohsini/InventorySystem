import mysql.connector
from databaseConnection import cursor, get_result_from_database
import sqlite3
from typing import Union
from classDefine import BuyersRow, CategoriesRow, InventoryRow, ManufacturersRow, ProductsRow, SuppliersRow, TransactionsRow, WarehousesRow

#1 2 3
def get_sales_quantity_categories(NTILENum):
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

#1 2 3
def get_sales_quantity_products(NTILENum):
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

# 4
def get_sales_quantity(start_date, end_date):  
  # query
  query = f"""
    SELECT 
        Products.ProductID,
        Products.ProductName,
        Categories.CategoriesID, 
        Categories.CategoriesName,
        Suppliers.SupplierID, 
        Suppliers.SupplierName,
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
  
  # if start_date and end_date:
  #   query += f'''
  #     WHERE 
  #         Transactions.TransactionsDate BETWEEN "{start_date}" AND "{end_date}"
  #     '''
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

#6 7 8
def get_profits():
  query = """
    SELECT 
      EXTRACT(YEAR FROM TransactionsDate) as Year, 
      EXTRACT(MONTH FROM TransactionsDate) as Month, Sum(Price*Quantity) as Revenue, 
      SUM(Cost*Quantity) as cost, 
      (SUM(Price*Quantity)-SUM(Cost*Quantity)) as Profit 
    FROM 
      Products 
    JOIN 
      Transactions ON Products.ProductID=Transactions.ProductID 
    GROUP BY 
      Year, Month 
    ORDER BY 
      Year, Month;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

#9
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

#15 好像不太有用
def get_avg_price_in_categories():
  query = """
    SELECT 
      c.CategoriesName, 
      AVG(p.Price) AS AvgPrice
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

#11
def get_product_out_of_stock():
  query = """
    SELECT 
      p.ProductName, 
      i.Quantity
    FROM 
      products p
    LEFT JOIN 
      inventory i ON p.ProductID = i.ProductID
    WHERE 
      i.Quantity = 0;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

#17-2
def get_stock():
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
      p.ProductID
  """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

#17
def get_stock_in_warehouse():
  query = """
    SELECT 
      w.State,
      w.City,
      p.ProductName,
      i.Quantity
    FROM 
      Products p
    JOIN 
      Inventory i ON p.ProductID = i.ProductID
    JOIN 
      Warehouses w ON i.WarehouseID = w.WarehouseID
    ORDER BY
      w.State,
      w.City
  """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

#18
def get_most_popular_categories():
  query = """
    SELECT 
      c.CategoriesName, 
      SUM(t.Quantity) AS TotalSold
    FROM 
      Categories c
    LEFT JOIN 
      Products p ON c.CategoriesID = p.CategoriesID
    LEFT JOIN 
      Transactions t ON p.ProductID = t.ProductID
    GROUP BY 
      c.CategoriesName
    ORDER BY 
      TotalSold DESC
    LIMIT 3;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# 19 20
def get_running_total_quantity():
  # query
  query = """
    SELECT 
      TransactionsDate,
      SUM(Quantity) OVER (ORDER BY TransactionsDate) AS Running_Total_Item,
      SUM(Products.Price * Transactions.Quantity) OVER (ORDER BY TransactionsDate) AS Running_Total_Value
    FROM 
      Transactions
    JOIN 
      Products ON Transactions.ProductID = Products.ProductID
    ORDER BY
      TransactionsDate;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

#21
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

#22
def get_avg_price_window():
  query = """
    SELECT 
      t.TransactionsDate,
      p.ProductName,
      AVG(Price) OVER (PARTITION BY p.ProductID ORDER BY TransactionsDate ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS Avg_price_over_3_transactions_period
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

#23
def get_buyer_ranking():
  query = """
    SELECT 
      BuyerID, 
      TransactionsDate,
      SUM(Quantity) OVER (PARTITION BY BuyerID ORDER BY TransactionsDate) AS Cumulative_Quantity
    FROM 
      Transactions;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

#24
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

#25
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

#26
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
    ) Subquery;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

#27
def get_transactions_num_per_month():
  query = """
    SELECT 
      DATE_FORMAT(TransactionsDate, '%Y-%m') AS Month,
      COUNT(TransactionsID) AS TransactionCount
    FROM 
      Transactions
    GROUP BY 
      Month
    ORDER BY 
      Month;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

#28 16
def get_product_info():
  query = """
    SELECT 
      t.ProductID, 
      MIN(t.TransactionsDate) AS FirstTransactionDate, 
      MAX(t.TransactionsDate) AS LastTransactionDate,
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
