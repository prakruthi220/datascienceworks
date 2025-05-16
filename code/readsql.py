import sqlite3 as sq3
import pandas as pd
con = sq3.Connection(r"C:\Users\DELL\Desktop\ml_codes\chinook.db") #create connection with the database
Cursor = con.cursor() #cursor object to interact with db
Cursor.execute("SELECT name FROM sqlite_master WHERE type='table';") #execution of the query to get tables
tables = Cursor.fetchall() #fetch all details
#for i in tables:print(i[0])
query = '''SELECT * FROM tracks''' #query for specific table
data = pd.read_sql(query,con)
print(data)
