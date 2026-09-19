import mysql.connector
import pandas as pd
import plotly.express as px


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

#plotly visualization
print("Generating plotly visual dashboards...")
fig_branch = px.bar(
    df_branches,
    x='branch_name',
    y='gross_revenue',
    color ='branch_name',
    title = 'Kilele Retail - Gross Revenue by Branch',
    labels = {'branch_name': 'Branch Location','gross_revenue': 'Gross Revenue (KES)'},
    text = 'gross_revenue'
)
fig_branch.update_traces(texttemplate='%{text:2s}',textposition = 'outside')

#saving the chart as a html

fig_branch.write_html("branch_revenue_chart.html")

#line chart for daily revenue trend
fig_daily = px.line(
    df_daily,
    x='transaction_date',
    y='daily_revenue',
    markers = True,
    title = 'Kilele Retail - Daily Revenue Trend Over Time',
    labels = {'transaction_date':'Transaction Date', 'daily_revenue':'Daily Revenue(KES)'}
) 

#saving our chart as html
fig_daily.write_html("daily_sales_trend.html")

fig_branch.show()
fig_daily.show()

db_connection.close()
print("Database connection successfully closed.")

