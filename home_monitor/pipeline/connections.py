
import csv
import sqlite3
import pandas as pd

# saving to a csv
def toCSV(input_data:list, file_name):

    with open(file_name, 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(input_data)
            
        
def toSqlite(query):
    con = sqlite3.connect('database/homemonitoring.db')
    cur = con.cursor()
    cur.execute(query)
    con.commit()

def fromSqlite(query):
    con = sqlite3.connect('database/homemonitoring.db')
    df = pd.read_sql(query, con)
    return df