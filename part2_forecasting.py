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
df_daily['day_index'] = np.arange(len(df_daily))


#fitting the linear regression model(OLS)
x= df_daily['day_index']
y = df_daily['daily_revenue']

slope,intercept = np.polyfit(x,y,1)
df_daily['trend_line'] = (slope * x) + intercept
print(f"calculated sales trend slope:{slope:.2f} KES per day")

#evaluate the accuracy of the model

y_mean = np.mean(y)
ss_total = np.sum((y-y_mean) ** 2)
ss_residual = np.sum((y-df_daily['trend_line']) ** 2)
r_squared = 1 - (ss_residual / ss_total)

print(f"Model r-squared(R2):{r_squared:.4f}")


#plotting and exporting with plotly
fig = px.scatter(
    df_daily,
    x='transaction_date',
    y='daily_revenue',
    title='kilele retail - daily sales and revenue trend model(R2= {r_squared:.2f})',
    labels = {'transaction date':'Transaction Date','daily_revenue':'Daily Revenue(KES)'}
)

fig.add_scatter(
    x=df_daily['transaction_date'],
    y = df_daily['trend_line'],
    mode='lines',
    name= 'Linear Trend Projection',
    line = dict(color='red',width = 3,dash='dash')
)

fig.write_html("sales_forecast_model.html")
print("Forecast model chart successfully saved as 'sales_forecast_model.html'!")
fig.show()
