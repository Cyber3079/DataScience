# Sales Analysis with Pandas

## Project Overview

This project analyses sales transaction data using Python and Pandas.

The goal is to extract useful business information from the dataset, identify sales trends, and practice fundamental data analysis techniques.

## Dataset

The dataset contains 20 sales transactions with the following information:

- Order ID
- Customer
- Product
- Category
- Quantity
- Unit Price
- Region
- Total Sales

## Tools Used

- Python
- Pandas
- CSV

## Analysis Performed

The following analysis was performed:

1. Loaded the sales data from a CSV file using Pandas.
2. Inspected the dataset using `head()`, `shape`, `info()`, and `describe()`.
3. Calculated total revenue using `sum()`.
4. Calculated total sales by product using `groupby()`.
5. Identified the best-selling product.
6. Identified the highest-value order.
7. Analysed total sales by region.
8. Compared average sales between product categories.
9. Identified the top 5 highest-value orders.

## Key Pandas Concepts Practiced

- `pd.read_csv()`
- `DataFrame`
- Selecting columns
- `head()`
- `shape`
- `info()`
- `describe()`
- `sum()`
- `mean()`
- `max()`
- `groupby()`
- `loc[]`
- `sort_values()`
- `head()`
- `idxmax()`
## Key Findings
The company generated R142,950 in total sales across the 20 orders analyzed.
Laptops were the best-performing product, generating R84,000, which was significantly higher than the other products.
Gauteng generated the highest regional sales at R70,550, followed by KwaZulu-Natal at R44,400.
Electronics had a much higher average order value of R11,760, compared with R2,535 for Accessories.
The highest-value order was ORD005, a laptop purchase worth R24,000.
The top five highest-value orders were primarily driven by laptop and monitor sales, suggesting that higher-priced products had a strong impact on overall revenue.
## Business Insight
The analysis suggests that high-value electronics, particularly laptops, are the main drivers of revenue. Gauteng is also the strongest-performing region, indicating that the company could investigate opportunities to expand sales in other regions while continuing to focus on high-value products.
## Project Structure

sales-analysis/
│
├── portfolio_sales_analysis.csv
├── sales_analysis.py
└── README.md