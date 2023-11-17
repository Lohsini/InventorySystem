# Inventory Database System Documentation

Welcome to our Inventory Database System! This system provides a user-friendly interface for querying and managing our inventory database. The system is divided into two main parts: Basic and Advanced. Additionally, at the end of this document, we will provide step-by-step instructions for building the entire project.

## Advanced SQL Query Video Demonstration
### Part 1: 
https://www.loom.com/share/662f86de5b7246b08d9ebcceb6a1d100
* 1:41 The explanation of the avg subtotals for each 3 transaction here has a mistake. This column means each row add three row of subtotals then divide by 3. It is a OLAP query.

### Part 2:
https://www.loom.com/share/e552931b38d64fa883cbb03ed913bdfb

## Basic Section
### Overview
In the basic section, users have access to fundamental CRUD (Create, Read, Update, Delete) operations. The user interface allows users to interact with different tables by providing the table name as a parameter. The available tables include:

- Categories
- Products
- Suppliers
- Manufacturers
- Buyers
- Warehouses
- Inventory
- Transactions

### Edit Mode
Users can enter edit mode by clicking the "Edit" button in the top right corner. Edit mode enables read-only operations. If there are errors during editing, users will receive error messages, allowing them to correct their actions.
To facilitate ease of use, a dropdown menu is provided for users to conveniently select various table ID options.

## Advanced Section
### Overview
In the advanced section, users can execute complex queries and generate different query reports based on specific scenarios. The following categories are available:

- Quantity Sold
- Revenue
- Ranking
- Stock
- Information
- Others

### Quantity Sold
- Quantity By Products: Provides information on the quantity sold for each product, allowing modification of NTILE.
- Quantity By Categories: Offers insights into the quantity sold for each categoryallowing modification of NTILE.
- Sales Quantity: Presents an overview of overall sales quantity, allowing modification of the date.

### Revenue
- Search Profits by Category: Allows users to search for profits based on category.
- Cumulative Revenue Group By Date: Displays cumulative revenue grouped by date.
- Average Subtotal Group By Date: Shows average subtotal grouped by date.
- Profits For Each Month: Provides information on profits for each month.
- State Revenue: Presents revenue data categorized by state.
- Total Revenue: Gives an overview of the total revenue.

### Ranking
- Buyer Ranking: Displays a ranking of buyers based on their transactions.
- Sales Ranking: Provides a ranking of products based on sales.
- No.1 Selling Product in Each Category (excluding products with a price <= 50): Identifies the best-selling product in each category, excluding low-priced products.

### Stock
- Stock In Warehouse: Shows the current stock in each warehouse.
- Product Stock: Provides information on the stock of each product.
- Product Out Of Stock: Identifies products that are out of stock.

### Information
- Product Information: Offers detailed information about each product.
- Buyer Information: Provides details about each buyer.
- Price Information In Each Categories: Presents pricing information for products in each 
category.

### Others
- Price Difference: Highlights differences in product prices.

This comprehensive Inventory Database System is designed to cater to both basic and advanced user needs. For any assistance or inquiries, please refer to the provided documentation or contact our support team.

## Instructions for building the project

### step 1:
- Open your command line and type the following code:
  ```
  git clone https://github.com/Lohsini/425TeamProject.git
  ```

### step 2:
- Check your current directory. Open a command line to navigate to the backend folder:
  ```
  cd SQL
  ```

### step 3:
- Refer to the 'README.md' for SQL instructions, where detailed steps for installing SQL files are provided.

### step 4:
- Check your current directory. Open a command line to navigate to the backend folder:
  ```
  cd backend
  ```

### step 5:
- Refer to the 'README.md' for backend instructions, where detailed steps for installing backend files are provided.

### step 6:
- Open another command line to navigate to the frontend folder:
  ```
  cd frontend
  ```

### step 7:
- Refer to the 'README.md' for frontend instructions, where detailed steps for installing frontend files are provided.
