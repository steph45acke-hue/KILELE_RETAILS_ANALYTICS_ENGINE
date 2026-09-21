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
    b.branch_id,
    b.branch_name,
    MAX(t.transaction_date) AS last_transaction_date,
    COUNT(DISTINCT t.transaction_id) AS frequency,
    SUM(t.total_amount) AS monetary
FROM branches b
JOIN transactions t ON b.branch_id = t.branch_id
GROUP BY b.branch_id, b.branch_name;
"""

df_rfm = pd.read_sql(rfm_query, db_connection)
db_connection.close()
print("Branch RFM raw data loaded successfully!\n")

#feature enginering(calculating recency)
df_rfm['last_transaction_date'] = pd.to_datetime(df_rfm['last_transaction_date'])
snapshot_date = df_rfm['last_transaction_date'].max() + pd.Timedelta(days=1)

df_rfm['recency'] = (snapshot_date - df_rfm['last_transaction_date']).dt.days

x_rfm = df_rfm[['recency','frequency','monetary']]
#standardization
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x_rfm)



Kmeans = KMeans(n_clusters=3,random_state=42,n_init=10)
df_rfm['cluster'] = Kmeans.fit_predict(x_scaled)

#3D visualization and plotly
fig = px.scatter_3d(
    df_rfm,
    x='recency',
    y='frequency',
    z='monetary',
    color='cluster',
    hover_name='branch_name',  # Changed from customer_name
    title='Kilele Retail - Branch Performance Segmentation (K-Means)',
    labels={'recency': 'Recency (Days Ago)', 'frequency': 'Frequency (Orders)', 'monetary': 'Monetary Revenue (KES)'}
)

fig.write_html("customer_segments_3d.html")
fig.show()
