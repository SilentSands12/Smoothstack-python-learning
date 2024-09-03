"""
Prompt
Assignment 4:

You have been given two datasets: sales_data.csv containing information about sales transactions
and customer_data.csv containing customer details. Your task is to use Pandas to clean the data,
perform necessary operations, and provide insights into the sales performance and customer behavior.

sales_data.csv Dataset Description:
Date: Date of the sale. Product: Name of the product sold. Price: Price of the product.
uantity: Quantity of the product sold. Customer ID: Unique identifier for the customer.

customer_data.csv Dataset Description:
Customer ID: Unique identifier for the customer. Name: Customer's full name. Age: Customer's age.
City: Customer's city.

Load and Clean Data:
Load both datasets into Pandas DataFrames. Check for missing values in both datasets and handle
them using dropna or fillna method. Ensure that both datasets have a common Customer ID column for merging.

Merge and Join:
Merge the cleaned sales data with the customer data using the Customer ID column. Perform an inner
join to combine the datasets based on the common customer IDs.

Data Analysis:
Calculate and display the total sales (Price * Quantity) for each transaction. Group the merged data
by City and find the total sales for each city. Determine the top-selling product based on the total quantity sold.

Assignment links

sales_data.csv
customers_data.csv
"""
import pandas as pd

# Step 1: Load the Data
sales_data = pd.read_excel('../sales_data.xlsx')
customer_data = pd.read_excel('../customers_data.xlsx')

# Step 2: Clean the Data
# Check for missing values
sales_data_missing = sales_data.isnull().sum()
customer_data_missing = customer_data.isnull().sum()

# Handle missing values
sales_data_cleaned = sales_data.dropna()  # or use fillna() if appropriate
customer_data_cleaned = customer_data.dropna()  # or use fillna() if appropriate

# Step 3: Merge the Data
merged_data = pd.merge(sales_data_cleaned, customer_data_cleaned, on='Customer ID', how='inner')

# Step 4: Data Analysis

# Calculate the total sales for each transaction
merged_data['Total Sales'] = merged_data['Price'] * merged_data['Quantity']

# Group by City and find the total sales for each city
sales_by_city = merged_data.groupby('City')['Total Sales'].sum().reset_index()

# Determine the top-selling product based on the total quantity sold
top_selling_product = merged_data.groupby('Product')['Quantity'].sum().reset_index().sort_values(by='Quantity', ascending=False).head(1)

# Display the results
print("Missing values in sales data:\n", sales_data_missing)
print("\nMissing values in customer data:\n", customer_data_missing)
print("\nTotal Sales by City:\n", sales_by_city)
print("Top Selling Product:\n", top_selling_product)


