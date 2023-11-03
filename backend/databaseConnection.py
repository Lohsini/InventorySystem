import mysql.connector
import password
import sqlite3
from typing import Union
from classDefine import BuyersRow, CategoriesRow, InventoryRow, ManufacturersRow, ProductsRow, SuppliersRow, TransactionsRow, WarehousesRow


# connect to local database
def connect_database():
  try:
    connection = mysql.connector.connect(
          host ="localhost",
          user ="root",
          password = password.password,
          database = "TeamProject"
        )
    
    return connection
  
  except mysql.connector.Error as err:
    print("Error: {}".format(err))
    
connection = connect_database()
cursor = connection.cursor()


# the assistance of read table
def get_result_from_database(result, cursor):
  # get column names
  column_names = [desc[0] for desc in cursor.description]

  # Iterate through the results and structure the data as dictionaries
  contents = []
  for row in result:
    content = dict(zip(column_names, row))
    contents.append(content)

  # return final result data
  data = {
    "headers": column_names,
    "contents": contents
  }
  return data

# read
def query_database_table(table_name):
  # query
  query = "SELECT * FROM {}".format(table_name)

  # execute
  cursor.execute(query)

  # get result
  result = cursor.fetchall()

  data = get_result_from_database(result, cursor)

  return data

# create
def create_new_row(table_name, item: Union[CategoriesRow,ProductsRow,SuppliersRow,ManufacturersRow,BuyersRow,WarehousesRow,InventoryRow,TransactionsRow]):
  try:
    if table_name == "categories":
      query = "INSERT INTO Categories (CategoriesID, CategoriesName, CategoriesDescription) VALUES (%s, %s, %s)"
      row = item.CategoriesID, item.CategoriesName, item.CategoriesDescription
    elif table_name == "products":
      query = "INSERT INTO Products (ProductID, ProductName, Price, Cost, CategoriesID, SupplierID, ManufacturerID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
      row = item.ProductID, item.ProductName, item.Price, item.Cost, item.CategoriesID, item.SupplierID, item.ManufacturerID
    elif table_name == "suppliers":
      query = "INSERT INTO Suppliers (SupplierID, SupplierName, ContactDetail_Phone, ContactDetail_Email) VALUES (%s, %s, %s, %s)"
      row = item.SupplierID, item.SupplierName, item.ContactDetail_Phone, item.ContactDetail_Email
    elif table_name == "manufacturers":
      query = "INSERT INTO Manufacturers (ManufacturerID, ManufacturerName, ContactDetail_Phone, ContactDetail_Email) VALUES (%s, %s, %s, %s)"
      row = item.ManufacturerID, item.ManufacturerName, item.ContactDetail_Phone, item.ContactDetail_Email
    elif table_name == "buyers":
      query = "INSERT INTO Buyers (BuyerID, name_Firstname, name_Lastname, ContactDetail_Phone, ContactDetail_Email) VALUES (%s, %s, %s, %s, %s)"
      row = item.BuyerID, item.name_Firstname, item.name_Lastname, item.ContactDetail_Phone, item.ContactDetail_Email
    elif table_name == "warehouses":
      query = "INSERT INTO Warehouses (WarehouseID, State, City) VALUES (%s, %s, %s)"
      row = item.WarehouseID, item.State, item.City
    elif table_name == "inventory":
      query = "INSERT INTO Inventory (ProductID, WarehouseID, Quantity) VALUES (%s, %s, %s)"
      row = item.ProductID, item.WarehouseID, item.Quantity
    elif table_name == "transactions":
      query = "INSERT INTO Transactions (TransactionsID, BuyerID, ProductID, Quantity, TransactionsDate) VALUES (%s, %s, %s, %s, %s)"
      row = item.TransactionsID, item.BuyerID, item.ProductID, item.Quantity, item.TransactionsDate

    cursor.execute(query, row)
    connection.commit()
    print("Create successfully.")
  except sqlite3.Error as e:
      print(f"An error occurred: {e}")

# delete
def delete_row(table_name, row_id):
  try:
    if table_name == "categories":
      query = "DELETE FROM Categories WHERE CategoriesID = %s"
    elif table_name == "products":
      query = "DELETE FROM Products WHERE ProductID = %s"
    elif table_name == "suppliers":
      query = "DELETE FROM Suppliers WHERE SupplierID = %s"
    elif table_name == "manufacturers":
      query = "DELETE FROM Manufacturers WHERE ManufacturerID = %s"
    elif table_name == "buyers":
      query = "DELETE FROM Buyers WHERE BuyerID = %s"
    elif table_name == "warehouses":
      query = "DELETE FROM Warehouses WHERE WarehouseID = %s"
    elif table_name == "transactions":
      query = "DELETE FROM Transactions WHERE TransactionsID = %s"

    cursor.execute(query, [row_id])
    connection.commit()
    print("Deleted successfully.")
  except sqlite3.Error as e:
      print(f"An error occurred: {e}")

# special delete
def delete_inventory(product_id, warehouse_id):
  try:
    query = "DELETE FROM Inventory WHERE ProductID = %s AND WarehouseID = %s"

    cursor.execute(query, (product_id, warehouse_id))
    connection.commit()
    print("Deleted successfully.")
  except sqlite3.Error as e:
      print(f"An error occurred: {e}")

# update
def update_row(table_name, item: Union[CategoriesRow,ProductsRow,SuppliersRow,ManufacturersRow,BuyersRow,WarehousesRow,InventoryRow,TransactionsRow]):
  try:
    if table_name == "categories":
      query = "UPDATE Categories SET CategoriesName = %s, CategoriesDescription = %s WHERE CategoriesID = %s"
      row = item.CategoriesName, item.CategoriesDescription, item.CategoriesID
    elif table_name == "products":
      query = "UPDATE Products SET ProductName = %s, Price = %s, Cost = %s, CategoriesID = %s, SupplierID = %s, ManufacturerID = %s WHERE ProductID = %s"
      row = item.ProductName, item.Price, item.Cost, item.CategoriesID, item.SupplierID, item.ManufacturerID, item.ProductID
    elif table_name == "suppliers":
      query = "UPDATE Suppliers SET SupplierName = %s, ContactDetail_Phone = %s, ContactDetail_Email = %s WHERE SupplierID = %s"
      row = item.SupplierName, item.ContactDetail_Phone, item.ContactDetail_Email, item.SupplierID
    elif table_name == "manufacturers":
      query = "UPDATE Manufacturers SET ManufacturerName = %s, ContactDetail_Phone = %s, ContactDetail_Email = %s WHERE ManufacturerID = %s"
      row = item.ManufacturerName, item.ContactDetail_Phone, item.ContactDetail_Email, item.ManufacturerID
    elif table_name == "buyers":
      query = "UPDATE Buyers SET name_Firstname = %s, name_Lastname = %s, ContactDetail_Phone = %s, ContactDetail_Email = %s WHERE BuyerID = %s"
      row = item.name_Firstname, item.name_Lastname, item.ContactDetail_Phone, item.ContactDetail_Email, item.BuyerID
    elif table_name == "warehouses":
      query = "UPDATE Warehouses SET State = %s, City = %s WHERE WarehouseID = %s"
      row = item.State, item.City, item.WarehouseID
    elif table_name == "inventory":
      query = "UPDATE Inventory SET Quantity = %s WHERE ProductID = %s"
      row = item.Quantity, item.ProductID
    elif table_name == "transactions":
      query = "UPDATE Transactions SET BuyerID = %s, ProductID = %s, Quantity = %s, TransactionsDate = %s WHERE TransactionsID = %s"
      row = item.BuyerID, item.ProductID, item.Quantity, item.TransactionsDate, item.TransactionsID

    cursor.execute(query, row)
    connection.commit()
    print("Updated successfully.")
  except sqlite3.Error as e:
      print(f"An error occurred: {e}")

# connection.close()