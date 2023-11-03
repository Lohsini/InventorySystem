#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mysql.connector
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from classDefine import (
    BuyersRow, CategoriesRow, InventoryRow, ManufacturersRow,
    ProductsRow, SuppliersRow, TransactionsRow, WarehousesRow
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define your database configuration
db_config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "database": "InventoryManagementSystem",
    "password": "admin1234"
}
# Function to connect to the database
def connect_to_db():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    return connection, cursor

# Function to close the database connection
def close_db(connection, cursor):
    cursor.close()
    connection.close()

# read_table API
@app.get("/tables/get/{table_name}")
def read_table(table_name: str):
    connection, cursor = connect_to_db()

    try:
        # Execute a SQL query to fetch data from the database
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchall()

        if not result:
            raise HTTPException(status_code=404, detail=f"{table_name} not found in the database")

        # Convert the result to a list of dictionaries
        table_data = []
        for row in result:
            table_data.append(dict(zip(data[table_name + '_header'], row)))

    finally:
        close_db(connection, cursor)

    return {
        "name": table_name,
        "headers": data[table_name + '_header'],
        "contents": table_data
    }

# create_row API
@app.post("/tables/create/{table_name}")
def create_row(table_name: str, new_content: dict):
    connection, cursor = connect_to_db()

    try:
        # Create and execute an SQL query to insert the new row into the database
        columns = ", ".join(new_content.keys())
        values = ", ".join(["%s"] * len(new_content))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        cursor.execute(query, list(new_content.values()))
        connection.commit()

    finally:
        close_db(connection, cursor)

    return {
        "name": table_name,
        "headers": data[table_name + '_header'],
        "contents": read_table(table_name)
    }

# delete_row API
@app.put("/tables/delete/{table_name}")
def delete_row(table_name: str, row_id: int):
    connection, cursor = connect_to_db()

    try:
        # Execute an SQL query to delete the row from the database
        query = f"DELETE FROM {table_name} WHERE {table_name}ID = %s"
        cursor.execute(query, (row_id,))
        connection.commit()

    finally:
        close_db(connection, cursor)

    return {
        "name": table_name,
        "headers": data[table_name + '_header'],
        "contents": read_table(table_name)
    }

# update_row API
@app.put("/tables/update/{table_name}/{row_id}")
def update_row(table_name: str, row_id: int, updated_content: dict):
    connection, cursor = connect_to_db()

    try:
        # Create and execute an SQL query to update the row in the database
        set_values = ", ".join([f"{key} = %s" for key in updated_content.keys()])
        query = f"UPDATE {table_name} SET {set_values} WHERE {table_name}ID = %s"
        cursor.execute(query, list(updated_content.values()) + [row_id])
        connection.commit()

    finally:
        close_db(connection, cursor)

    return {
        "name": table_name,
        "headers": data[table_name + '_header'],
        "contents": read_table(table_name)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

