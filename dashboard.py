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
    