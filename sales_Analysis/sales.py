import pandas as pd

df=pd.read_csv('C:/Users/matlh/Desktop/DataScience/sales_Analysis/portfolio_sales_analysis.csv')

print(df.head()) #shows the first 5 entries

print(df.shape) #rows X columns

print(df.describe()) # shows mean,median, mode,quantile,max,min

df.info()

print(df['Total_Sales'].sum()) #shows total amount sales

product=df.groupby('Product')['Total_Sales'].sum() #groups product by name anad shows the sum of each prd
print(product.max()) # shows the price of Product that gens more sales

print(df.loc[df['Total_Sales']==df['Total_Sales'].max(),['Order_ID','Customer','Product','Category','Quantity','Total_Sales']])

print(df.groupby('Region')['Total_Sales'].sum())

print(df.groupby('Category')['Total_Sales'].mean())
sort_price=df['Total_Sales'].sort_values(ascending=False)
print(sort_price.head(5))