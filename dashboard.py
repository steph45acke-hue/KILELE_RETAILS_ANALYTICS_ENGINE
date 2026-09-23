import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

st.set_page_config(
    page_title="Kilele Retails Analytics Engine",
    page_icon="📊",
    layout="wide"
)

st.title("🛒 Kilele Retails Analuytics & Intelligence Engine")
st.markdown("Operartional dashboard connecting MySQL relational data, sales trends, and machine learning branch segmentation.")

# Connecting to my SQL Database
@st.cache_resource
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='stephen0111301468',
        database='kilele_retail_db', 
    )

try:
    conn = get_db_connection()
except Exception as e:
    st.error(f"Database connection failed:{e}")
    st.stop()

# Sidebar navigation and filters
st.sidebar.header("Navigation & Filters")
app_mode = st.sidebar.selectbox("Choose View", ["Executive Overview", "Branch Performance Clusters", "Sales Trend Forecasting"])

branches_df = pd.read_sql("SELECT branch_id, branch_name FROM branches;", conn)
branch_options = ["All Branches"] + list(branches_df['branch_name'])
selected_branch = st.sidebar.selectbox("Filter by Branch", branch_options)

# Executive Overview
if app_mode == "Executive Overview":
    st.subheader("📈 Executive KPI Summary")

    kpi_query = """
    SELECT
      COUNT(t.transaction_id) AS total_transactions,
      SUM(t.quantity_sold) AS total_units,
      SUM(t.total_amount) AS gross_revenue
    FROM transactions t
    """
    if selected_branch != "All Branches":
        branch_id_val = branches_df[branches_df['branch_name'] == selected_branch]['branch_id'].values[0]
        kpi_query += f" WHERE t.branch_id = '{branch_id_val}'"

    kpi_df = pd.read_sql(kpi_query, conn)

    col1, col2, col3 = st.columns(3)
    col1.metric("Gross Revenue", f"KES {kpi_df['gross_revenue'].values[0]:,.2f}")
    col2.metric("Total Transactions", f"{kpi_df['total_transactions'].values[0]:,}")
    col3.metric("Units Sold", f"{kpi_df['total_units'].values[0]:,}")

    st.markdown("---")

    branch_rev_query = """
    SELECT b.branch_name, SUM(t.total_amount) AS revenue
    FROM transactions t
    JOIN branches b ON t.branch_id = b.branch_id
    GROUP BY b.branch_name
    ORDER BY revenue DESC;
    """
    branch_rev_df = pd.read_sql(branch_rev_query, conn)

    fig_branch = px.bar(
        branch_rev_df,
        x='branch_name',
        y='revenue',
        color='branch_name',
        title="Gross Revenue by Branch Location",
        labels={'branch_name': 'Branch', 'revenue': 'Revenue (KES)'}
    )

    st.plotly_chart(fig_branch, use_container_width=True)

# Branch performance clusters (Machine Learning)
elif app_mode == "Branch Performance Clusters":
    st.subheader("🤖 Machine Learning: Branch Performance Segmentation (K-Means)")
    st.markdown("Grouping Kilele's branches using Recency, Frequency, and Monetary (RFM) metrics.") 

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
    df_rfm = pd.read_sql(rfm_query, conn)

    df_rfm['last_transaction_date'] = pd.to_datetime(df_rfm['last_transaction_date'])
    snapshot_date = df_rfm['last_transaction_date'].max() + pd.Timedelta(days=1)
    df_rfm['recency'] = (snapshot_date - df_rfm['last_transaction_date']).dt.days

    X_rfm = df_rfm[['recency', 'frequency', 'monetary']]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_rfm)

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df_rfm['cluster'] = kmeans.fit_predict(X_scaled)

    st.dataframe(df_rfm[['branch_name', 'recency', 'frequency', 'monetary', 'cluster']], use_container_width=True)
    
    fig_3d = px.scatter_3d(
        df_rfm,
        x='recency',
        y='frequency',
        z='monetary',
        color='cluster',
        hover_name='branch_name',
        title='3D Branch Performance Clusters',
        labels={'recency': 'Recency (Days)', 'frequency': 'Frequency (Orders)', 'monetary': 'Monetary (KES)'}
    )
    st.plotly_chart(fig_3d, use_container_width=True)

elif app_mode == "Sales Trend Forecasting":
    st.subheader("📅 Daily Sales Trend Analysis")
        
    trend_query = """
    SELECT 
        transaction_date,
        SUM(total_amount) AS daily_revenue,
        SUM(quantity_sold) AS daily_units
    FROM transactions
    GROUP BY transaction_date
    ORDER BY transaction_date ASC;
    """
    trend_df = pd.read_sql(trend_query, conn)
        
    fig_trend = px.line(
        trend_df,
        x='transaction_date',
        y='daily_revenue',
        markers=True,
        title='Daily Revenue Progression',
        labels={'transaction_date': 'Date', 'daily_revenue': 'Revenue (KES)'}
    )
    st.plotly_chart(fig_trend, use_container_width=True)