import databaseConnection

data = {
    "categories_header": ["CategoriesID", "CategoriesName", "CategoriesDescription"],
    "products_header": ["ProductID", "ProductName", "Price", "Cost", "CategoriesID", "SupplierID", "ManufacturerID"],
    "suppliers_header": ["SupplierID", "SupplierName", "ContactDetail_Phone", "ContactDetail_Email"],
    "manufacturers_header": ["ManufacturerID", "ManufacturerName", "ContactDetail_Phone", "ContactDetail_Email"],
    "buyers_header": ["BuyerID", "name_Firstname", "name_Lastname", "ContactDetail_Phone", "ContactDetail_Email"],
    "warehouses_header": ["WarehouseID", "State", "City"],
    "inventory_header": ["ProductID", "WarehouseID", "Quantity"],
    "transactions_header": ["TransactionsID", "BuyerID", "ProductID", "Quantity", "TransactionsDate"],
    "categories": [
        {"CategoriesID": 1, "CategoriesName": "Category 1", "CategoriesDescription": "Description 1"},
        {"CategoriesID": 2, "CategoriesName": "Category 2", "CategoriesDescription": "Description 2"},
    ],
    "products": [
        {"ProductID": 1, "ProductName": "Product 1", "Price": 10.99, "Cost": 5.99, "CategoriesID": 1, "SupplierID": 1, "ManufacturerID": 1},
        {"ProductID": 2, "ProductName": "Product 2", "Price": 15.99, "Cost": 8.99, "CategoriesID": 2, "SupplierID": 2, "ManufacturerID": 2},
    ],
    "suppliers": [
        {"SupplierID": 1, "SupplierName": "Supplier 1", "ContactDetail_Phone": "123-456-7890", "ContactDetail_Email": "supplier1@example.com"},
        {"SupplierID": 2, "SupplierName": "Supplier 2", "ContactDetail_Phone": "987-654-3210", "ContactDetail_Email": "supplier2@example.com"},
    ],
    "manufacturers": [
        {"ManufacturerID": 1, "ManufacturerName": "Manufacturer 1", "ContactDetail_Phone": "111-222-3333", "ContactDetail_Email": "manufacturer1@example.com"},
        {"ManufacturerID": 2, "ManufacturerName": "Manufacturer 2", "ContactDetail_Phone": "444-555-6666", "ContactDetail_Email": "manufacturer2@example.com"},
    ],
    "buyers": [
        {"BuyerID": 1, "name_Firstname": "John", "name_Lastname": "Doe", "ContactDetail_Phone": "555-123-4567", "ContactDetail_Email": "john.doe@example.com"},
        {"BuyerID": 2, "name_Firstname": "Jane", "name_Lastname": "Smith", "ContactDetail_Phone": "777-987-6543", "ContactDetail_Email": "jane.smith@example.com"},
    ],
    "warehouses": [
        {"WarehouseID": 1, "State": "California", "City": "Los Angeles"},
        {"WarehouseID": 2, "State": "New York", "City": "New York City"},
    ],
    "inventory": [
        {"ProductID": 1, "WarehouseID": 1, "Quantity": 100},
        {"ProductID": 2, "WarehouseID": 1, "Quantity": 50},
    ],
    "transactions": [
        {"TransactionsID": 1, "BuyerID": 1, "ProductID": 1, "Quantity": 10, "TransactionsDate": "2023-10-30"},
        {"TransactionsID": 2, "BuyerID": 2, "ProductID": 2, "Quantity": 5, "TransactionsDate": "2023-10-31"},
    ]
}


