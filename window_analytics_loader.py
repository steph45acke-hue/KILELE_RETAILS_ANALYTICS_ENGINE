import pandas as pd
import streamlit as st
import plotly.express as px
from sqlalchemy import create_engine

def render_window_analytics_dashboard():
    st.subheader("📊 Advanced Window Analytics & Sales Velocity")
    st.markdown("Leveraging SQL window functions (`ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LEAD`) to analyze granular product performance and branch transaction momentum.")

    # 1. Establish Database Connection
   
    try:
        engine = create_engine("mysql+mysqlconnector://root:stephen0111301468@localhost/kilele_retail_db")
        conn = engine.connect()
    except Exception as e:
        st.error(f"Database Connection Error: {e}")
        return

    # 2. Tabs for Partitioned Rankings vs Branch Velocity
    tab1, tab2 = st.tabs(["🏆 Category Product Rankings", "⚡ Branch Sales Momentum (LEAD)"])

    with tab1:
        st.markdown("### Category-Specific Product Leaderboards")
        st.markdown("Each category maintains its own independent ranking, preventing high-ticket items from overshadowing everyday products.")

        rank_query = """
        SELECT 
            c.category_name,
            p.product_name,
            SUM(t.total_amount) AS total_revenue,
            ROW_NUMBER() OVER (PARTITION BY c.category_name ORDER BY SUM(t.total_amount) DESC) AS row_num,
            RANK() OVER (PARTITION BY c.category_name ORDER BY SUM(t.total_amount) DESC) AS item_rank,
            DENSE_RANK() OVER (PARTITION BY c.category_name ORDER BY SUM(t.total_amount) DESC) AS dense_item_rank
        FROM transactions t
        JOIN products p ON t.product_id = p.product_id
        JOIN categories c ON p.category_id = c.category_id
        GROUP BY c.category_name, p.product_name;
        """
        df_rankings = pd.read_sql(rank_query, conn)

        # Category Filter Selectbox
        selected_category = st.selectbox(
            "Filter by Product Category:", 
            df_rankings["category_name"].unique()
        )

        filtered_rankings = df_rankings[df_rankings["category_name"] == selected_category]

        # Plotly Bar Chart Visual
        fig = px.bar(
            filtered_rankings.head(5), 
            x="product_name", 
            y="total_revenue", 
            color="item_rank",
            title=f"Top 5 Products in {selected_category} (Partitioned Ranking)",
            labels={"product_name": "Product Name", "total_revenue": "Total Revenue (KES)", "item_rank": "Rank"}
        )
        st.plotly_chart(fig, use_container_width=True)

        # Detailed Table View
        with st.expander("Inspect Full Partitioned Ranking Table"):
            st.dataframe(filtered_rankings[["product_name", "total_revenue", "row_num", "item_rank", "dense_item_rank"]], use_container_width=True)

    with tab2:
        st.markdown("### Branch Transaction Acceleration")
        st.markdown("Tracking chronological revenue changes between consecutive sales at individual branches using the `LEAD()` function.")

        lead_query = """
        SELECT 
            b.branch_name,
            t.transaction_date,
            t.total_amount AS current_sale_amount,
            LEAD(t.total_amount, 1) OVER (PARTITION BY b.branch_id ORDER BY t.transaction_date ASC) AS next_sale_amount,
            (LEAD(t.total_amount, 1) OVER (PARTITION BY b.branch_id ORDER BY t.transaction_date ASC) - t.total_amount) AS revenue_difference
        FROM transactions t
        JOIN branches b ON t.branch_id = b.branch_id
        ORDER BY b.branch_name, t.transaction_date ASC;
        """
        df_lead = pd.read_sql(lead_query, conn)

        # Branch Filter Selectbox
        selected_branch = st.selectbox(
            "Select Branch for Velocity Analysis:", 
            df_lead["branch_name"].unique()
        )

        filtered_lead = df_lead[df_lead["branch_name"] == selected_branch]
        st.dataframe(filtered_lead.head(15), use_container_width=True)

    # Close connection
    conn.close()


if __name__ == "__main__":
    render_window_analytics_dashboard()