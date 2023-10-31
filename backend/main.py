from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from classDefine import BuyersRow, CategoriesRow, InventoryRow, ManufacturersRow, ProductsRow, SuppliersRow, TransactionsRow, WarehousesRow
from mockData import data

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], # allow all for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# read_table API
@app.get("/tables/get/{table_name}")
def read_table(table_name: str):
    return {
        "name": table_name,
        "headers": data[table_name+'_header'],
        "contents": data[table_name]
    }

# create_row API
@app.post("/tables/create/{table_name}")
def create_row(table_name: str, new_content: Union[CategoriesRow,ProductsRow,SuppliersRow,ManufacturersRow,BuyersRow,WarehousesRow,InventoryRow,TransactionsRow]):
    if table_name in data:
      data[table_name].append(new_content)
      return {
          "name": table_name,
          "headers": data[table_name+'_header'],
          "contents": data[table_name]
      }

# delete_row API
@app.put("/tables/delete/{table_name}")
def delete_row(table_name: str, row_index: int):
    if table_name in data:
      table_data = data[table_name]
      if 0 <= row_index < len(table_data):
        table_data.pop(row_index)
        return {
            "name": table_name,
            "headers": data[table_name+'_header'],
            "contents": data[table_name]
        }

# update_row API
@app.post("/tables/update/{table_name}")
def update_row(table_name: str, row_index: int, new_content: Union[CategoriesRow,ProductsRow,SuppliersRow,ManufacturersRow,BuyersRow,WarehousesRow,InventoryRow,TransactionsRow]):
    if 0 <= row_index < len(data[table_name]):
      data[table_name][row_index] = new_content
      return {
          "name": table_name,
          "headers": data[table_name+'_header'],
          "contents": data[table_name]
      }
