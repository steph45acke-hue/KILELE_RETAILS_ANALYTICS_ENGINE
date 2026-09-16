import mysql.connector
import pandas as pd
import streamlit as st

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

 

