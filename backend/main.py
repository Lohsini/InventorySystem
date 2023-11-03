from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from classDefine import BuyersRow, CategoriesRow, InventoryRow, ManufacturersRow, ProductsRow, SuppliersRow, TransactionsRow, WarehousesRow
import databaseConnection
import databaseAdvanced

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], # allow all for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------- basic -----------
# read_table API
@app.get("/tables/get/{table_name}")
def read_table(table_name: str):
  query_result = databaseConnection.query_database_table(table_name)
  return {
    "name": table_name,
    "headers": query_result["headers"],
    "contents": query_result["contents"],
  }

# create_row API
@app.post("/tables/create/{table_name}")
def create_row(table_name: str, new_content: Union[CategoriesRow,ProductsRow,SuppliersRow,ManufacturersRow,BuyersRow,WarehousesRow,InventoryRow,TransactionsRow]):
  databaseConnection.create_new_row(table_name, new_content)
  return new_content

# delete_row API
@app.put("/tables/delete/inventory/{product_id}/{warehouse_id}")
def delete_inventory(product_id: str, warehouse_id: str):
    databaseConnection.delete_inventory(product_id, warehouse_id)

# delete_row API
@app.put("/tables/delete/{table_name}/{row_id}")
def delete_row(table_name: str, row_id: str):
    databaseConnection.delete_row(table_name, row_id)
    return table_name

# update_row API
@app.post("/tables/update/{table_name}")
def update_row(table_name: str, new_content: Union[CategoriesRow,ProductsRow,SuppliersRow,ManufacturersRow,BuyersRow,WarehousesRow,InventoryRow,TransactionsRow]):
    databaseConnection.update_row(table_name, new_content)
    return "ok"

# ----------- advanced -----------
@app.get("/advanced/sales_quantity")
def get_sales_quantity():
  query_result = databaseAdvanced.get_sales_quantity()
  return query_result

@app.get("/advanced/products_NTILE")
def get_products_NTILE():
  query_result = databaseAdvanced.get_products_NTILE()
  return query_result


