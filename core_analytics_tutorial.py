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

print("Here is our aggregated branch revenue dataframe:")
print(df_branch_summary,"\n")

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







