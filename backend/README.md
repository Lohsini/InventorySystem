# 425databaseproject

# backend

### step 1:
install the environment:
```
pip install -r requirements.txt
```

### step 2: 
use the command line to run main.py
```
python main.py
```
### step 3 :
On line 15 in "databaseConnection.py", change the database string parameter to the match the name of your database.

### step 4 :
On line 14 in "databaseConnection.py", change the password string parameter to the match the password of your database.

### step 5 :
use the command line to try the API
```
uvicorn main:app --reload
or
python uvicorn main:app --reload
```

### step 6:
go to http://127.0.0.1:8000/docs#/ is easier for you to test API.

## Editing steps

### step 1:
open main.py, the main API code is inside.

you can write the code for api to deliver the data here.

### step 2:
open main.py, the main database code are inside.

you can write the code for getting database here.

