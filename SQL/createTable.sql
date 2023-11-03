create Database TeamProject;
use TeamProject;

CREATE TABLE Categories (
    CategoriesID VARCHAR(3) PRIMARY KEY,
    CategoriesName VARCHAR(255),
    CategoriesDescription TEXT
);
CREATE TABLE Suppliers (
    SupplierID VARCHAR(3) PRIMARY KEY,
    SupplierName VARCHAR(255),
    ContactDetail_Phone VARCHAR(20),
    ContactDetail_Email VARCHAR(255)
);
CREATE TABLE Buyers (
    BuyerID VARCHAR(3) PRIMARY KEY,
    name_Firstname VARCHAR(255),
    name_Lastname VARCHAR(255),
    ContactDetail_Phone VARCHAR(20),
    ContactDetail_Email VARCHAR(255)
);
CREATE TABLE Manufacturers (
    ManufacturerID VARCHAR(3) PRIMARY KEY,
    ManufacturerName VARCHAR(255),
    ContactDetail_Phone VARCHAR(20),
    ContactDetail_Email VARCHAR(255)
);
CREATE TABLE Warehouses (
    WarehouseID VARCHAR(3) PRIMARY KEY,
    State VARCHAR(255),
    City VARCHAR(255)
);
CREATE TABLE Products (
    ProductID VARCHAR(3) PRIMARY KEY,
    ProductName VARCHAR(255),
    Price DECIMAL(10, 2),
    Cost DECIMAL(10, 2),
    CategoriesID VARCHAR(3),
    SupplierID VARCHAR(3),
    ManufacturerID VARCHAR(3),
    FOREIGN KEY (CategoriesID) REFERENCES Categories(CategoriesID) ON DELETE CASCADE,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE,
    FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID) ON DELETE CASCADE
);
CREATE TABLE Inventory (
    ProductID VARCHAR(3),
    WarehouseID VARCHAR(3),
    Quantity INT,
    PRIMARY KEY (ProductID, WarehouseID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (WarehouseID) REFERENCES Warehouses(WarehouseID) ON DELETE CASCADE
);
CREATE TABLE Transactions (
    TransactionsID VARCHAR(3) PRIMARY KEY,
    BuyerID VARCHAR(3),
    ProductID VARCHAR(3),
    Quantity INT,
    TransactionsDate DATETIME,
    FOREIGN KEY (BuyerID) REFERENCES Buyers(BuyerID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);