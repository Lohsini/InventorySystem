# Backend Instructions

## Part 1: Project Setup

### step 1:
- Install the required environment dependencies using the following command:
  ```
  pip install -r requirements.txt
  ```

### step 2: 
- Run the main backend application using the command line:
  ```
  python main.py
  ```
### step 3 :
- In "databaseConnection.py" at line 14, update the password string parameter to match the password of your database.

### step 4 :
- In "databaseConnection.py" at line 15, update the database string parameter to match the name of your database.

### step 5 :
- Test the API using the command line:
  ```
  uvicorn main:app --reload
  ```
- Alternatively, you can use:
  ```
  python uvicorn main:app --reload
  ```

### step 6:
- Navigate to http://127.0.0.1:8000/docs#/ for an easier way to test the API.


## Part2: Editing steps and backend code Introduction

### step 1:
- Open "main.py" to access the main API code. You can write the code for API to deliver the data in this file.

### step 2:
- Open "main.py" to access the main database code. You can write the code for getting database information in this file.

### step 3:
- Open "databaseConnection.py" to access basic CRUD functions, and each query is present within the respective function. Relevant parameters can be inputted as needed.

### step 4:
- Open "databaseAdvanced.py" to access advanced queries. Each query is encapsulated within its corresponding function, often modified based on the specifications outlined in our group's deliverable 3. Some queries are new and complex, with parameters available for customization.