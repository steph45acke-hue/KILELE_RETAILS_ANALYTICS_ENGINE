import mysql.connector
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import plotly.express as px

db_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "stephen0111301468",
    database = "kilele_retail_db"
)

#extracting rfm data via sql aggregation

rfm_query = """
  SELECT
     c.customer_id,
     c.customer_name,
     MAX(t.transaction_date) AS last_purchase_date,
     COUNT(DISTINCT t.transaction_id) AS frequency,
     SUM(t.total_amount) AS monetary
FROM customers c
JOIN transactions t ON c.customer_id = t.customer_id
GROUP BY c.customer_id,c.customer_name;
"""

df_rfm = pd.read_sql(rfm_query,db_connection)
db_connection.close()

#feature enginering(calculating recency)
df_rfm['last_purchase_date'] = pd.to_datetime(df_rfm['last_purchase_date'])
snapshot_date = df_rfm['last_purchase_date'].max() + pd.Timedelta(days=1)
df_rfm['receny'] = (snapshot_date - df_rfm['last_purchase_date']).dt.days

x_rfm = df_rfm[['recency','frequency','monetary']]
