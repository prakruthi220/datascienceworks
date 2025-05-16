import sqlite3 as sq3
import pandas as pd
import pandas.io.sql as pds
import seaborn as sns

con = sq3.Connection(r"C:\Users\DELL\Desktop\classic_rock.db")

cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print(tables)
query = '''
SELECT Song, AVG(PlayCount) AS avg_plays  
    FROM rock_songs
    ORDER BY avg_plays;
'''
ob = pd.read_sql(query,con)
print(ob)
sns.boxplot(x='avg_plays', data=ob) 

