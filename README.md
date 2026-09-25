# Kilele Retails Analytics Engine

## Project Description
Welcome to the **Kilele Retails Analytics Engine**! This is a complete, portfolio-grade data science and engineering project built from scratch to manage, process, and visualize multi-branch retail store operations. Imagine running a retail business with locations across Westlands, CBD, Langata, and Kasarani. This application aggregates raw sales data, stores it securely in a relational database, applies advanced SQL analytics and machine learning clustering, and displays everything on an interactive web application designed for executive decision-making.

---

## The Reason Behind It
The primary goal of building this project is to bridge the gap between raw data collection and executive-level business intelligence. Having theoretical knowledge is not enough when trying to land a data science job; recruiters and hiring managers want proof that you can handle data from end to end—from designing local database schemas and writing complex queries to implementing machine learning models and deploying a production-ready web application.

---

## The Problem Involved
In traditional retail environments, data is often fragmented across isolated files or basic spreadsheets. When managers need to evaluate store performance, they face several roadblocks:
* Basic database groupings (`GROUP BY`) only provide surface-level summaries without capturing deep behavioral insights.
* High-ticket items frequently skew overall product rankings, overshadowing everyday fast-moving consumer goods.
* Tracking sequential sales momentum and daily revenue changes across different branch timelines requires manual, error-prone calculations.
* Stakeholders lack a centralized, interactive interface to automatically monitor key performance indicators (KPIs) and machine learning branch clusters.

---

## The Solution
This project introduces a unified, automated analytics pipeline that solves these operational challenges:
1. **Relational Database Storage**: Centralizes all branches, categories, products, and transactions in a structured MySQL database.
2. **Advanced SQL Architecture**: Employs partitioned window functions (`ROW_NUMBER`) for fair product leaderboards and lead-lag analysis (`LEAD`) to track sequential transaction revenue deltas.
3. **Machine Learning Branch Segmentation**: Utilizes unsupervised K-Means clustering to group retail outlets using Recency, Frequency, and Monetary (RFM) behavioral metrics.
4. **Interactive Dashboard Deployment**: Packages all back-end logic into a multi-view Streamlit and Plotly application featuring executive summaries, dynamic filters, and 3D cluster visualizations.

---

## Step-by-Step Implementation & Visual Screenshot Walkthrough

### Phase 1: Relational Database Architecture & SQL Extraction
* **What we did**: We set up a normalized relational database in MySQL Workbench (`kilele_retail_db`), creating connected tables for branches, categories, products, and transactions, and executed multi-table SQL joins to extract baseline operational metrics.
* **Beginner Explanation**: Think of this as building a well-organized digital filing cabinet. Every piece of sales information connects cleanly to its respective store branch and product category so nothing gets lost.

![MySQL Workbench Data Extraction View](Screenshot%20(259).jpg)

* **Detailed Interview Explanation**: This interface represents the foundational data engineering tier of the project. By writing explicit multi-table joins (`JOIN branches`, `JOIN categories`, `JOIN products`), we pull raw transactional records into a clean, unified result grid containing exact timestamps, branch identifiers, and monetary totals.

---

### Phase 2: Advanced SQL Window Functions & Time Series Analysis
* **What we did**: We wrote advanced analytical queries using window functions (`ROW_NUMBER() OVER (PARTITION BY...)` and `LEAD() OVER (PARTITION BY...)`) directly inside MySQL Workbench.
* **Beginner Explanation**: Standard database groupings lump everything together. Window functions let us look at specific subsets—like ranking products *only inside their own grocery aisle* so expensive specialty items don't overshadow everyday essentials. The `LEAD()` function acts like a time-travel tool, peeking at the very next transaction to show whether sales are accelerating or slowing down.

![Partitioned Ranking Analysis](Screenshot%20(260).jpg)

![Lead-Lag Trend Analysis](Screenshot%20(261).jpg)

* **Detailed Interview Explanation**: These queries prove advanced SQL proficiency. The first screenshot utilizes `ROW_NUMBER() OVER (PARTITION BY c.category_name...)` to isolate top-performing products inside each category independently without price distortion. The second screenshot deploys the `LEAD()` window function partitioned by branch ID to preview subsequent sale amounts and calculate exact revenue deltas between sequential transactions.

---

### Phase 3: Machine Learning Segmentation & Predictive Modeling (3D Clusters)
* **What we did**: We applied unsupervised machine learning (K-Means Clustering) to segment retail branches using multi-dimensional behavioral metrics (Recency, Frequency, and Monetary value - RFM).
* **Beginner Explanation**: Instead of guessing which stores act alike, we fed store performance metrics into an algorithm that automatically groups them into behavioral clusters, plotted live in a rotating 3D space.

![3D Branch Performance Clusters](Screenshot%20(258).png)

* **Detailed Interview Explanation**: This interface connects data science modeling directly to commercial operations. By feeding multi-dimensional RFM metrics into a K-Means clustering algorithm, the system automatically categorizes retail branches into operational groups, visualized in an interactive 3D scatter plot to help stakeholders evaluate behavioral segmentation.

---

### Phase 4 & 5: Development Environment, Terminal Scripts & Exploratory Analytics
* **What we did**: We managed code development inside VS Code, running Python scripts to clean dataframes, manage database connections, and test our pipeline components.
* **Beginner Explanation**: This is the kitchen where all the ingredients are prepped. Before building any user interface, we tested our database pipelines line-by-line in the code editor to guarantee absolute data integrity.

![VS Code Development Environment](Screenshot%20(259).jpg)

* **Detailed Interview Explanation**: Utilizing VS Code alongside Python ensures robust software engineering practices. Writing modular scripts to handle data validation and database handshakes prevents bugs from breaking downstream user applications and ensures seamless data transfer.

---

### Phase 6: Production Streamlit Dashboard Deployment (`app_v1.py`)
* **What we did**: We deployed a fully functional, multi-view Streamlit web application (`localhost:8501`) featuring a sidebar navigation pane, executive KPI summary cards, interactive 3D cluster charts, and dynamic category filters.
* **Beginner Explanation**: This is the final product—a polished, professional web application where stakeholders can open a browser, review overall earnings, and interact with live charts instantly.

![Executive Overview Dashboard](Screenshot%20(257).png)

![Sales Trend Forecasting](Screenshot%20(256)_2.png)

![Category Product Leaderboards](Screenshot%20(262)_2.png)

* **Detailed Interview Explanation**: This dashboard bridges raw backend logic with executive decision-making. The high-level KPI cards communicate immediate commercial health (tracking total gross revenue of **KES 85,150.00**, 19 transactions, and 295 units sold), while dynamic sidebar toggles let leadership pivot seamlessly between daily sales trend forecasting and category-specific product leaderboards (*Cereals & Flour*, *Cooking Oils & Fats*, *Fresh Dairy*, *Tea & Hot Drinks*).

---

## Technology Involved
* **Database Management**: MySQL, MySQL Workbench
* **Data Processing & Modeling**: Python, Pandas, NumPy, Scikit-Learn
* **Data Visualization & Web App**: Plotly, Streamlit
* **Development Environment & Version Control**: VS Code, Git, GitHub

---

## How to Use It

To run this project locally on your machine, follow these simple steps:

1. **Clone the Repository**:
   ```bash
   git clone [https://github.com/steph45acke-hue/KILELE_RETAILS_ANALYTICS_ENGINE.git](https://github.com/steph45acke-hue/KILELE_RETAILS_ANALYTICS_ENGINE.git)
   cd KILELE_RETAILS_ANALYTICS_ENGINE
Install Required Python Dependencies:

Bash
pip install -r requirements.txt
Configure Your Local Database:

Set up your local MySQL instance and import the kilele_retail_db schema.

Update your database connection strings in the configuration files.

Launch the Streamlit Dashboard:

Bash
streamlit run app_v1.py

