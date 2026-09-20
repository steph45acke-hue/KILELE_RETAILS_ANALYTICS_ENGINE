import mysql.connector
import pandas as pd
import plotly.express as px


print("---connecting to mysql and fetching data---")

#establishing our connection
db_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="stephen0111301468",
    database = "kilele_retail_db"
)

print("Database connection established successfully!\n")


#writing our aggregated query
aggregated_query = """
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
df_branch_summary = pd.read_sql(aggregated_query,db_connection)
#calculating executive KPIs using pandas 
total_gross_revenue = df_branch_summary['gross_revenue'].sum()
total_units = df_branch_summary['total_units_sold'].sum()
top_branch = df_branch_summary.iloc[0]['branch_name']
top_branch_revenue = df_branch_summary.iloc[0]['gross_revenue']

#a clean executive summary dashboard
print("kilele retail executive summary kpi's")
print(f"Total Gross Revenue:KES {total_gross_revenue:,.2f}")
print(f"Total units sold:{total_units:,} units ")
print("Top-Performing Branch:{top_branch} (KES {top_branch_revenue:,.2f})")


#creating an interactive plotly bar chart
print("Generating plotly interactive chart")
fig = px.bar(
    df_branch_summary,
    x='branch_name',
    y='gross_revenue',
    color='branch_name',
    title='Gross revenue by branch',
    labels = {'branch_name':'Branch Location','gross_revenue':'Gross Revenue(KES)'},
    text = 'gross_revenue'
)

fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')


#saving the chart as a html file
output_filename = "tutorial_branch_chart.html"
fig.write_html(output_filename)
print(f"Chart successfully saved as '{output_filename}'!")

fig.show()

db_connection.close()
print("\nDatabase connection closed safely.")







