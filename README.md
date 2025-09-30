# Approximate Query Processing
Using PostgreSQL and Python to create approximations of averages on datasets with different distributions.

This readme is a work in progress and any changes can be made as needed to reflect the current state of the project.

# Setup

## To install psycopg: 

With python installed (in this example I am using python3), you should be able to use the command `python3 -m pip install psycopg`


## Testing the connection:
To use the test directory, to test if your python connection is working:
1. Create a database called university 
2. Run DDL.sql to create the relations
3. Run smallRelationsInsertFile.sql to insert test data
4. Make a user called `python` and with a password `pythonConnection`, or change the username and password in  `test.py`
5. Run the python file `test.py` 
