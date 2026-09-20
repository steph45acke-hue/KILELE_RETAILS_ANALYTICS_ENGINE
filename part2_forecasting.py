import mysql.connector
import pandas as pd
import numpy as np
import plotly.express as px


#opening the database connection
db_connection = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = "stephen0111301468",
    database = "kilele_retail_db"
)

#extracting aggregated data via sql
daily_query = """
SELECT
  t.transaction_date,
  SUM(t.total_amount) AS daily_revenue
FROM transactions t
GROUP BY t.transaction_date
ORDER BY t.transaction_date ASC;
"""

df_daily = pd.read_sql(daily_query,db_connection)
db_connection.close()
print("Daily sales data successfully loaded for modeling!\n")


#data preprocessing and numerical indexing
df_daily['transaction_date'] = pd.to_datetime(df_daily['transaction_date'])
