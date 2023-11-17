from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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

class DateTime(BaseModel):
    start_date: str
    end_date: str

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
@app.post("/advanced/quantity_sold")
def get_quantity_sold(dateTime: DateTime):
  query_result = databaseAdvanced.get_quantity_sold(dateTime.start_date, dateTime.end_date)
  return query_result

@app.get("/advanced/quantity_sold/categories/{NTILENum}")
def get_quantity_sold(NTILENum: int):
  query_result = databaseAdvanced.get_quantity_sold_categories(NTILENum)
  return query_result

@app.get("/advanced/quantity_sold/products/{NTILENum}")
def get_quantity_sold(NTILENum: int):
  query_result = databaseAdvanced.get_quantity_sold_products(NTILENum)
  return query_result

@app.get("/advanced/cumulative_revenue_in_date")
def get_cumulative_revenue_in_date():
  query_result = databaseAdvanced.get_cumulative_revenue_in_date()
  return query_result

@app.get("/advanced/avg_subtotal_window")
def get_avg_subtotal_window():
  query_result = databaseAdvanced.get_avg_subtotal_window()
  return query_result

@app.get("/advanced/buyer_ranking")
def get_buyer_ranking():
  query_result = databaseAdvanced.get_buyer_ranking()
  return query_result

@app.get("/advanced/price_difference")
def get_price_difference():
  query_result = databaseAdvanced.get_price_difference()
  return query_result

@app.get("/advanced/rank1_product_in_categories")
def get_rank1_product_in_categories():
  query_result = databaseAdvanced.get_rank1_product_in_categories()
  return query_result

@app.get("/advanced/state_revenue")
def get_state_revenue():
  query_result = databaseAdvanced.get_state_revenue()
  return query_result

@app.get("/advanced/product_info")
def get_product_info():
  query_result = databaseAdvanced.get_product_info()
  return query_result

@app.get("/advanced/sales_rank")
def get_sales_rank():
  query_result = databaseAdvanced.get_sales_rank()
  return query_result

@app.get("/advanced/profits")
def get_profits():
  query_result = databaseAdvanced.get_profits()
  return query_result

@app.get("/advanced/buyer_info")
def get_buyer_info():
  query_result = databaseAdvanced.get_buyer_info()
  return query_result

@app.get("/advanced/product_out_of_stock")
def get_product_out_of_stock():
  query_result = databaseAdvanced.get_product_out_of_stock()
  return query_result

@app.get("/advanced/price_info_in_categories")
def get_price_info_in_categories():
  query_result = databaseAdvanced.get_price_info_in_categories()
  return query_result

@app.get("/advanced/stock_in_warehouse")
def get_stock_in_warehouse():
  query_result = databaseAdvanced.get_stock_in_warehouse()
  return query_result

@app.get("/advanced/product_stock")
def get_product_stock():
  query_result = databaseAdvanced.get_product_stock()
  return query_result

@app.get("/advanced/product_stock")
def get_product_stock():
  query_result = databaseAdvanced.get_product_stock()
  return query_result


@app.get("/advanced/total_revenue")
def get_total_revenue():
  query_result = databaseAdvanced.get_total_revenue()
  return query_result
