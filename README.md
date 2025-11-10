# Approximate Query Processing
Using PostgreSQL and Python to create approximations of averages on datasets with different distributions.

This readme is a work in progress and any changes can be made as needed to reflect the current state of the project.

# Setup

## To install required packages: 

With python installed (in this example I am using python3), you should be able to use the command `python3 -m pip install -r requirements.txt`. If you are using VSCode and are in a venv, you can just do `pip install -r requirements.txt` Doing it the first way will install the packages globally on your computer. The second way keeps it narrowed to the environment using it. You can follow [this link](https://code.visualstudio.com/docs/python/environments) to see how to create a virtual environment in VSCode.

***NOTE: Any packages you add will have to be manually added to the `requirements.txt` file, and you will have to manually invoke it when the file is changed.***


## Testing the connection:
To use the test directory, to test if your python connection is working:
1. [Create a database](https://www.postgresql.org/docs/current/tutorial-createdb.html) called aqp_database 
2. Run DDL.sql to create the relations
3. Run smallRelationsInsertFile.sql to insert test data
4. Make a user called `python` and with a password `pythonConnection`, or change the username and password in  `test.py`
5. Run the python file `test.py` 

## Running database_operations files:
(*) Ensure that the username and password are correct in `.env`. The default is the username `python` and password `pythonConnection`. If you have a username with that password, no updates are needed. This allows you to update the username and password combination in one place and it will apply everywhere. 
(*) Before running any of the files in this folder, run the following commands
    1. GRANT USAGE ON SCHEMA public TO python
    2. GRANT CREATE ON SCHEMA public TO python