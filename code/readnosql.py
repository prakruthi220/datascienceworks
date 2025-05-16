from PyMango import MongoClient
import pandas as pd

con = MongoClient()
con.list_database_names()
db = con.database_name
cursor = db.collection_name.find(query)
df = pd.DataFrame(list(cursor))
