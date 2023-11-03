import mysql.connector
from databaseConnection import cursor, get_result_from_database
import sqlite3
from typing import Union
from classDefine import BuyersRow, CategoriesRow, InventoryRow, ManufacturersRow, ProductsRow, SuppliersRow, TransactionsRow, WarehousesRow


def get_sales_quantity():
  query = ""
  
  # query
  query = """
    SELECT Categories.CategoriesID, Categories.CategoriesName, SUM(Transactions.Quantity) as Total_Products_Purchased
    FROM Transactions 
    JOIN Products ON Transactions.ProductID = Products.ProductID 
    JOIN Categories ON Products.CategoriesID = Categories.CategoriesID 
    GROUP BY Categories.CategoriesID, Categories.CategoriesName
    ORDER BY Total_Products_Purchased DESC;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()
  print(result)

  data = get_result_from_database(result, cursor)

  return data


def get_sales_quantity():
  query = ""
  
  # query
  query = """
    SELECT Categories.CategoriesID, Categories.CategoriesName, SUM(Transactions.Quantity) as Total_Products_Purchased
    FROM Transactions 
    JOIN Products ON Transactions.ProductID = Products.ProductID 
    JOIN Categories ON Products.CategoriesID = Categories.CategoriesID 
    GROUP BY Categories.CategoriesID, Categories.CategoriesName
    ORDER BY Total_Products_Purchased DESC;
    """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

def get_products_NTILE():
  query = ""
  
  # query
  query = """
    SELECT Products.ProductID, Products.ProductName, Categories.CategoriesName, SUM(Transactions.Quantity) as Total_Purchased,
    NTILE(4) OVER (ORDER BY SUM(Transactions.Quantity) DESC) as Quartile FROM Transactions JOIN Products ON 
    Transactions.ProductID = Products.ProductID JOIN Categories ON Products.CategoriesID = Categories.CategoriesID
    GROUP BY Products.ProductID, Products.ProductName, Categories.CategoriesName ORDER BY Total_Purchased DESC;
  """
  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data