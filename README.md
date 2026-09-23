# E-Commerce Sales Analytics

## 📌 Project Overview

This project analyzes e-commerce sales data to understand sales performance, profitability, product performance, and regional trends.

SQL was used for data exploration and business analysis, Python/Pandas was used for analytical processing and AI integration, while Power BI was used to build an interactive dashboard for visualizing key performance indicators and business insights. An Ollama-powered local LLM was integrated to enable natural-language business queries.

## 🎯 Objectives

- Analyze overall sales and profit performance
- Identify the best-performing categories and sub-categories
- Identify loss-making products
- Analyze sales volume and profitability
- Compare actual sales with monthly targets
- Identify top-performing states and cities
- Build an interactive Power BI dashboard

## 🛠️ Tools & Technologies

- **SQL / MySQL** – Data analysis and business queries
- **Power BI** – Data visualization and dashboard development
- **Power Query** – Data cleaning and transformation
- **DAX** – Calculated columns and Power BI analysis
- **Python / Pandas** – AI analytics and data processing
- **Ollama / Llama 3.2** – Local LLM for natural-language business queries

## 📂 Dataset

The project uses three datasets:

- `Order Details.csv` – Contains order-level sales, quantity, category, sub-category, and profit information.
- `List of Orders.csv` – Contains order dates and geographical information such as state and city.
- `Sales target.csv` – Contains monthly sales targets by category.

## 🔍 Analysis Performed

### SQL Analysis

The following analyses were performed using SQL:

- Total sales, profit, and quantity
- Category-wise sales and profit
- Sub-category-wise sales and profit
- Highest and lowest profit sub-categories
- Top-selling sub-categories
- Loss-making sub-categories
- Profit margin analysis
- High-sales but loss-making products
- Top 3 sub-categories by sales

### Power BI Dashboard

The Power BI dashboard includes:

- Total Sales KPI
- Total Profit KPI
- Total Quantity KPI
- Sales by Category
- Sales by Sub-Category
- Profit by Category
- Profit by Sub-Category
- Sales vs Profit by Category
- Sales Trend
- Top 5 States by Sales
- Top 5 Cities by Sales
- Monthly Sales vs Target
- Interactive category filters

## 🤖 AI-Powered Analytics

An AI layer was integrated into the project using Python, Pandas, Ollama, and Llama 3.2.

The system allows users to ask business questions in natural language, such as:

- Which category has the highest sales?
- Which category has the highest profit?
- Which state has the highest profit?
- Which sub-category is making a loss?
- Give me an overall business summary.

### How It Works

User asks a business question  
↓  
Ollama / Llama 3.2 interprets the question  
↓  
Selects the appropriate predefined Python analytical function  
↓  
Python / Pandas calculates the result from the project dataset  
↓  
The result is passed back to the LLM  
↓  
AI provides a business-oriented explanation

The numerical calculations are performed by Python/Pandas rather than allowing the LLM to generate numerical values directly.

## 📊 Key Insights

- **Electronics** generated the highest total sales.
- **Clothing** generated the highest total profit among categories.
- **Printers** generated the highest sales and profit among sub-categories.
- **Saree** had the highest quantity sold.
- **Tables** generated the highest overall loss.
- **Electronic Games** generated more than ₹30,000 in sales but still resulted in a loss.
- **Clothing** had the highest profit margin among the three categories.
- The dashboard compares **actual monthly sales against sales targets** to evaluate performance.

## 📈 Dashboard

The Power BI dashboard consists of two pages:

### Page 1 – E-Commerce Sales & Profit Analysis

Provides an overview of sales, profit, quantity, category performance, and sub-category profitability.
![E-Commerce Sales & Profit Analysis](Dashboard/dashboard_page%201.png)

### Page 2 – E-Commerce Sales Performance & Target Analysis

Provides sales trends, top-performing states and cities, and monthly sales versus target analysis.
![E-Commerce Sales Performance & Target Analysis](Dashboard/dashboard_page%202.png)

## 💡 Business Recommendations

- Investigate the reasons behind losses in the **Tables** sub-category.
- Review pricing, discounting, and cost structure for loss-making products.
- Focus on high-margin categories and products.
- Monitor monthly sales against targets to identify underperforming periods.
- Analyze high-sales but low-profit products to improve profitability.
