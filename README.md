# Kilele Retail Analytics Engine: Executive Presentation Deck

---

## 1. Project Description
We built a smart retail analytics system called the **Kilele Retail Analytics Engine**. It is a complete, end-to-end data pipeline connecting a structured MySQL relational database (`kilele_retail_db`) with automated Python analytics scripts and an interactive Streamlit operational dashboard. This system allows store managers and executives to track real-time store performance, analyze daily revenue momentum, monitor branch profitability, and view top-selling products through dynamic web visualizations[cite: 37, 38, 39, 40, 41, 42, 43, 44, 45, 46].

---

## 2. The Problem Involved
Before this system was developed, retail data was scattered and fragmented across local files and manual sheets. Store managers had no unified, real-time way to compare how different branches—such as Westlands, CBD, Lang'ata, and Kasarani—were performing against one another[cite: 40]. Furthermore, standard analytical tools suffered from a major product distortion flaw: high-ticket items (like bulk cooking oil or premium goods) always dominated standard charts, completely overshadowing and hiding everyday essential commodities (like milk, sugar, or tea bags) from management view.

---

## 3. The Reason Behind It
The primary goal of this project was to bridge the gap between raw data storage and actionable business intelligence. To succeed in modern data science, we needed a robust portfolio project that demonstrates end-to-end mastery—spanning from raw database schema design and advanced SQL window functions to clean Python backends and professional, dark-themed executive data storytelling dashboards.

---

## 4. The Solution Involved
* **Relational Database Architecture:** Designed and deployed a robust multi-table relational database in MySQL Workbench covering branches, categories, products, and transactions to ensure zero data duplication[cite: 31, 36].
* **Advanced SQL Analytics:** Implemented advanced SQL window functions (such as `ROW_NUMBER() OVER (PARTITION BY ...)` and `LEAD()`) to partition product rankings within categories and compute day-over-day revenue velocity[cite: 41, 42].
* **Interactive Streamlit Dashboard:** Deployed a fully responsive web application featuring executive KPI summaries, branch performance clusters, linear regression forecasting, and category-partitioned product leaderboards[cite: 35, 43, 44, 45, 46].

---

## 5. Comprehensive Screenshot Walkthrough (Boss-Level Storytelling)

Below is the complete visual breakdown of every single screenshot captured during our project development, explained in clear, executive-ready language for the boss:

### 1. Daily Sales Trend Over Time (CBD Branch)
> **`Screenshot (229).png` Story:** *"Boss, when we look at our CBD branch (`CBD_01`) on our interactive sidebar filter, this line chart tracks our daily sales trend over time. It shows a steady climb from late August, peaking nicely around August 30th before a brief mid-week dip and a strong rebound by September 3rd[cite: 28]. This helps us spot exactly when foot traffic peaks in the central business district."*

![Screenshot (229).png](name=Screenshot (229).png)

### 2. Daily Sales Trend Over Time (Westlands Branch)
> **`Screenshot (230).png` Story:** *"Switching our filter to the Westlands branch (`WST_02`), our sales tracker tells a completely different, high-value story[cite: 29]. We see a massive revenue peak right at the end of August (hitting nearly 9,000 KES), followed by a steady flow that dips mid-week[cite: 29]. This visibility allows us to adjust inventory stocking specifically for high-volume weekends."*

![Screenshot (230).png](name=Screenshot (230).png)

### 3. Daily Sales Trend Over Time (Kasarani Branch)
> **`Screenshot (231).png` Story:** *"Here, boss, we are examining the Kasarani branch (`KSR_03`)[cite: 30]. The trend line highlights steady, reliable daily performance hovering between 2,500 and 4,000 KES, with an upward recovery trajectory heading into Thursday, September 3rd[cite: 30]. It proves that Kasarani maintains a very stable, predictable baseline of daily customer purchases."*

![Screenshot (231).png](name=Screenshot (231).png)

### 4. Daily Sales Trend Over Time (Lang'ata Branch)
> **`Screenshot (232).png` Story:** *"Moving over to the Lang'ata branch (`LNG_04`), this line chart maps our sales velocity across late August and early September[cite: 37]. Notice how sales climb sharply from a dip on August 31st to peak at nearly 7,000 KES mid-week on September 2nd[cite: 37]. This gives us clear insight into localized buying patterns in the southern suburbs."*

![Screenshot (232).png](name=Screenshot (232).png)

### 5. Top Products Revenue Breakdown (CBD Branch)
> **`Screenshot (233).png` Story:** *"Boss, this view pairs our transaction table with a product revenue breakdown for our CBD location[cite: 38]. Items like *Supa Dafra Rice 5kg* lead the store's revenue contribution at 6,500 KES[cite: 38], proving that bulk essential grains drive heavy retail traffic right in the center of town."*

![Screenshot (233).png](name=Screenshot (233).png)

### 6. MySQL Daily Sales Performance Query
> **`Screenshot (243).png` Story:** *"Behind every great dashboard is clean database architecture. Here in MySQL Workbench, we executed a daily sales performance query grouping transactions by date[cite: 31]. This query aggregates total transactions, units sold, and daily gross revenue, giving our backend absolute mathematical accuracy[cite: 31]."*

![Screenshot (243).png](name=Screenshot (243).png)

### 7. VS Code Python Analytics Terminal Output (Products & Branches)
> **`Screenshot (244).png` & `Screenshot (245).png` Story:** *"Boss, here is our Python analytics engine running live inside VS Code[cite: 32, 33]. The script connects straight to our MySQL database using Pandas, executing automated reports for Product Performance and Branch Revenue Summary[cite: 33]. We can see right in the terminal that Kilele Westlands leads branch revenue at 29,800 KES while Supa Dafra Rice leads product revenue at 27,950 KES[cite: 33]."*

![Screenshot (244).png](name=Screenshot (244).png)
![Screenshot (245).png](name=Screenshot (245).png)

### 8. Streamlit Executive Overview & KPI Summary
> **`Screenshot (257).png` Story:** *"Welcome to the main executive landing page of our web app! Here, our KPI summary card instantly tells the boss the big picture: total enterprise gross revenue stands at an impressive 85,150 KES across 19 transactions and 295 units sold[cite: 34]. Below it, the bar chart ranks our branch locations instantly[cite: 34]."*

![Screenshot (257).png](name=Screenshot (257).png)

### 9. Branch Performance Clusters & 3D Visualization
> **`Screenshot (258).png` Story:** *"Boss, this is where data science meets management. We applied K-Means clustering to segment our branches based on Recency, Frequency, and Monetary (RFM) metrics[cite: 35]. The 3D scatter plot visualizes how our branches group together, giving us a scientific way to identify top-tier locations versus stores needing strategic intervention[cite: 35]."*

![Screenshot (258).png](name=Screenshot (258).png)

### 10. Master Relational Data Extraction (MySQL)
> **`Screenshot (259).png` Story:** *"This MySQL query represents our master relational data extraction[cite: 36]. By joining branches, categories, products, and transactions into a single unified grid[cite: 36], we ensure that every single data point on our dashboard traces back to a verified, immutable transaction record."*

![Screenshot (259).png](name=Screenshot (259).png)

### 11. Enterprise Daily Revenue Trend Chart
> **`Screenshot (246).png` Story:** *"Zooming out to enterprise view, this line chart maps total daily revenue across all stores[cite: 39]. It clearly captures our massive market surge hitting over 16k KES on September 2nd following an end-of-month dip on September 1st[cite: 39], helping us plan cash flow accordingly."*

![Screenshot (246).png](name=Screenshot (246).png)

### 12. Gross Revenue by Branch Comparison Chart
> **`Screenshot (247).png` Story:** *"If you want to know our heavy lifters at a glance, this executive bar chart ranks our four stores[cite: 40]. Kilele Westlands leads the enterprise at 29.8k KES, followed by CBD at 23.5k KES, Lang'ata at 17.2k KES, and Kasarani at 14.65k KES[cite: 40]."*

![Screenshot (247).png](name=Screenshot (247).png)

### 13. Product Ranking by Category (MySQL Window Functions)
> **`Screenshot (260).png` Story:** *"Boss, in this SQL query, we utilized the `ROW_NUMBER() OVER (PARTITION BY c.category_name ORDER BY SUM(t.total_amount) DESC)` window function[cite: 41]. This ensures products are ranked independently inside their own categories so high-ticket items don't distort our reports[cite: 41]."*

![Screenshot (260).png](name=Screenshot (260).png)

### 14. Chronological Branch Sales & Lead-Lag Analysis (MySQL)
> **`Screenshot (261).png` Story:** *"This advanced SQL query uses the `LEAD()` window function to preview upcoming transaction amounts and calculate day-over-day `revenue_difference`[cite: 42]. It gives us immediate predictive visibility into momentum shifts at the branch level[cite: 42]."*

![Screenshot (261).png](name=Screenshot (261).png)

### 15. Category-Specific Product Leaderboard (Cereals & Flour)
> **`Screenshot (262).png` & `Screenshot (263).png` Story:** *"Boss, looking at our Streamlit category leaderboards, filtering by *Cereals & Flour* isolates staples like Supa Dafra Rice, Kabras Sugar, and Jogoo Unga[cite: 43, 44]. Notice how clean this is—everyday essentials finally get their own spotlight without being overshadowed[cite: 43, 44]."*

![Screenshot (262).png](name=Screenshot (262).png)
![Screenshot (263).png](name=Screenshot (263).png)

### 16. Category Leaderboard (Cooking Oils & Fats)
> **`Screenshot (264).png` Story:** *"When we switch our category filter to *Cooking Oils & Fats*, the dashboard instantly isolates *Baraka Cooking Oil 3L* as the undisputed category leader with over 15k KES in recorded revenue[cite: 45]."*

![Screenshot (264).png](name=Screenshot (264).png)

### 17. Category Leaderboards (Fresh Dairy & Tea/Hot Drinks)
> **`Screenshot (265).png` Story:** *"Finally, looking at daily essentials, our *Fresh Dairy* filter highlights *Brookside Fresh Milk 500ml*, and switching to *Tea & Hot Drinks* isolates *Kericho Gold Tea 500g*[cite: 46]. The color-graded rank scale on the right gives us an instant visual cue of market dominance within each product group[cite: 46]."*

![Screenshot (265).png](name=Screenshot (265).png)

---

## 6. The Technology Behind It
* **Python:** Core programming language used for data manipulation and backend scripting.
* **Streamlit:** Modern web framework used to build and deploy the interactive executive dashboard.
* **Plotly:** Advanced charting library used to render responsive, dark-themed visual graphics.
* **MySQL & MySQL Workbench:** Enterprise relational database management system used for schema normalization and SQL querying.
* **Pandas & NumPy:** Data science libraries utilized for tabular data processing and machine learning clustering.

---

## 7. How to Use It
1. **Clone the Repository:** Pull the project repository from GitHub (`KILELE_RETAILS_ANALYTICS_ENGINE`).
2. **Start MySQL:** Ensure your local MySQL server is active with the `kilele_retail_db` schema fully loaded.
3. **Run the Application:** Open your terminal in VS Code or PyCharm and execute the command:
   ```bash
   streamlit run app_v1.py
Interact: Open your browser at localhost:8501 to explore branch filters, category leaderboards, and live executive analytics[cite: 28].