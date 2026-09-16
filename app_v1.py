import mysql.connector
import pandas as pd
import streamlit as st
import plotly.express as px

#page configuration and header
st.set_page_config (
    page_title = "Kilele Retail Analytics Engine",page_icon="🛒",layout="wide"

)

st.title("🛒 Kilele Retails Analytics Engine")
st.subheader("Tier 1: Basic Branch Retrieval & Filtering")


#database connection
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost", user="root", password="stephen0111301468", database="kilele_retail_db"
    )
    return conn
#  Sidebar Filters for User Interactivity
st.sidebar.header("🔍 Filter Controls")
selected_branch = st.sidebar.selectbox(
    "Select Nairobi Branch", ["CBD_01", "WST_02", "KSR_03", "LNG_04"]
)

#  Writing the SQL Query
query = f"""
    SELECT 
        t.transaction_id, 
        b.branch_name,
        p.product_name, 
        t.quantity_sold, 
        t.total_amount, 
        t.transaction_date
    FROM transactions t
    INNER JOIN products p ON t.product_id = p.product_id
    INNER JOIN branches b ON t.branch_id = b.branch_id
    WHERE t.branch_id = '{selected_branch}'
    ORDER BY t.total_amount DESC;
"""

#  Fetching  Data from MySQL into a Pandas DataFrame 
try:
  conn = get_db_connection()
  df = pd.read_sql(query, conn)
  conn.close()
except Exception as e:
  st.error(f"Error connecting to database: {e}")
  st.stop()
   
#calculating key metrics
total_revenue = df["total_amount"].sum() if not df.empty else 0
total_transactions = len(df)


#displaying metric cards

col1,col2 = st.columns(2)
with col1:
    st.metric(
        label="Total Transactions",
        value = total_transactions,
        help = "Number of sales records found for this branch",
    
    )
with col2:
    st.metric(
        label = "Total Revenue (KES)",
        value = f" KES {total_revenue:,.2f}",
        help = "Combined sales value for this selection",
    )

    #rendering the interactive table
st.markdown("---")
st.markdown(f"### Transaction Records for Branch: `{selected_branch}`")

# Render the interactive data table
st.dataframe(df,use_container_width = True)

 
#adding a visual trend chart
st.markdown("---")
st.markdown(f"### Top Products Revenue Breakdown:'{ selected_branch}'")

if not df.empty:
   chart_data = (
      df.groupby("product_name")["total_amount"].sum().reset_index()
   )

   chart_data = chart_data.set_index("product_name")
   st.bar_chart(chart_data)
else:
     st.info("No transaction data available to plot for this branch.")
# . Add a Date-Based Line Chart for Sales Trends Over Time
st.markdown("---")
st.markdown(f"### 📈 Daily Sales Trend Over Time: `{selected_branch}`")

if not df.empty:
 
  df["transaction_date"] = pd.to_datetime(df["transaction_date"])

  
  trend_data = (
      df.groupby("transaction_date")["total_amount"].sum().reset_index()
  )

 
  trend_data = trend_data.set_index("transaction_date")

  st.line_chart(trend_data)
else:
  st.info("No transaction data available for trend analysis.")


#advanced interactive plotly trend chart
st.markdown("---")
st.markdown(
   f"### 🚀Advanced interactive sales trend(plotly):'{selected_branch}'"
)

if not df.empty:
   df["transaction_date"] = pd.to_datetime(df["transaction_date"])
   trend_data = (
      df.groupby("transaction_date")["total_amount"].sum().reset_index()
   )

   trend_data.sort_values("transaction_date")
   fig = px.line(
      trend_data,
      x="transaction_date",
      y="total_amount",
      markers = True,
      title =f"Daily Revenue Velocity - {selected_branch}",
      labels = {
         "transaction_date": "Transaction Date",
         "total_amount":"Revenue(KES)",
      },
   )

   # Customize layout for a clean appearance and sharp tooltips
   fig.update_layout(
      xaxis_title="Date",
      yaxis_title="Total Revenue (KES)",
      hovermode="x unified",
  )

   st.plotly_chart(fig,use_container_width=True)
else:
   st.info("No transaction data available for advanced interactive plotting.")

#finding the minimum and maximum dates available for this branch's data
if not df.empty:
   min_date = pd.to_datetime(df["transaction_date"]).min().date()
   max_date = pd.to_datetime(df["transaction_date"]).max().date()

   