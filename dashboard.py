import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


st.set_page_config(
    page_title = "Kilele Retails Analytics Engine",
    page_icon="📊",
    layout ="wide"
)

st.title("🛒 Kilele Retails Analuytics & Intelligence Engine")
st.markdown("Operartional dashboard connecting MySQL relational data,sales trends,and machine learning branch segmentation.")

#connecting to my SQL Database
@st.cache_resource
def get_db_connection():
    return mysql.connector.connect(
       host = 'localhost',
       user = 'root',
       password = 'stephen0111301468',
       database = 'kilele_retail_db', 
    )

try:
    conn = get_db_connection()
except Exception as e:
    st.error(f"Database connection failed:{e}")
    st.stop()

#side bar navigation and filters
st.sidebar.header("Navigation & Filters")
app_mode = st.sidebar.selectbox("Choose View",["Executive Overview","Branch Performance Clusters","Sales Trend Forecasting"])



branches_df = pd.read_sql("SELECT branch_id,branch_name FROM branches;" conn)
branch_options = ["All Branches"] + list(branches_df['branch_options'])
selected_branch = st.sidebar.selectbox("Filter by Branch",branch_options)

#executive overview
if app_mode == "Executive Overview":
    st.subheader("📈 Executive KPI Summary")

    kpi_query ="""
SELECT
  COUNT(t.transaction_id) AS total_transactions,
  SUM(t.quantity_sold) AS total_units,
  SUM(t.total_amount) AS gross_revenue
FROM transactions t
"""
if selected_branch != "All Branches":
    branch_id_val = branches_df[branches_df['branch_name'] == selected_branch]['branch_id'].values[0]
    kpi_query += f"WHERE t.branch_id = '{branch_id_val}'"

    kpi_df = pd.read_sql(kpi_query,conn)
    