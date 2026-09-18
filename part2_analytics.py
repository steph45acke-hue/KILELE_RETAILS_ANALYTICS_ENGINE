import mysql.connector
import pandas as pd

#establishing our connection
db_connection = mysql.connector.connect(
    host = "localhost",
    user="root",
    password = "stephen0111301468",
    database = "kilele_retail_db"
)

#writing our sql query as a multi line string
product_query = """
SELECT
    p.product_name,
    p.unit_price,
    COUNT(t.transaction_id) AS times_ordered,
    SUM(t.quantity_sold) AS total_units_sold,
    SUM(t.total_amount) AS total_product_revenue
FROM transactions t
INNER JOIN products p ON t.product_id = p.product_id
GROUP BY p.product_name,p.unit_price
ORDER BY total_product_revenue DESC;
"""


df_products = pd.read_sql(product_query,db_connection)
print("--- Product Performance Report ---")
print(df_products,"\n")

#branch revenue summary
branch_query = """
SELECT 
    b.branch_name,
    COUNT(t.transaction_id) AS total_transactions,
    SUM(t.quantity_sold) AS total_units_sold,
    SUM(t.total_amount) AS gross_revenue
FROM transactions t
INNER JOIN branches b ON t.branch_id = b.branch_id
GROUP BY b.branch_name
ORDER BY gross_revenue DESC;
"""
df_branches = pd.read_sql(branch_query,db_connection)

print("--- Branch revenue summary ---")
print(df_branches,"\n")

#daily performance trend
daily_query ="""
SELECT
   t.transaction_date,
   COUNT(t.transaction_id) AS daily_transactions,
   SUM(t.quantity_sold) AS daily_units_sold,
   SUM(t.total_amount) AS daily_revenue
FROM transactions t
GROUP BY t.transaction_date
ORDER BY t.transaction_date ASC;
  
"""
df_daily = pd.read_sql(daily_query, db_connection)
print("---3.Daily sales performance trend---")
print(df_daily,"\n")



db_connection.close()
print("Database connection successfully closed.")


