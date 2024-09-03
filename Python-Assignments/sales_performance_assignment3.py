"""
Prompt
Assignment 3:

You have been given a CSV file named data.csv containing information about sales transactions.
Your task is to use Python and the Pandas library to analyze the data and provide insights into the sales performance.

Dataset Description:

data.csv contains the following columns: Date, Product, Price, Quantity, Customer ID. Each row
represents a sales transaction with the date of the sale, the product name, the price of the product,
the quantity sold, and the customer ID.

Tasks:
Load Data:
Use Pandas to read the data.csv file and load it into a Pandas DataFrame.

Data Exploration:
Display the first 5 rows of the DataFrame to understand the structure of the data. Check for
missing values in each column and handle them appropriately. Determine the number of unique products in the dataset.

Data Analysis: Calculate and display the total sales (Price * Quantity) for each transaction.
Calculate the overall sales for each product. Find out the best-selling product (product with the highest total sales).

Time-based Analysis: Convert the Date column to a Pandas datetime object. Extract and create
new columns for Year, Month, and Day from the Date column. Calculate the total sales for each year and month.
Identify the month with the highest sales.

Customer Analysis: Determine the number of unique customers in the dataset. Calculate and display
the average purchase amount per customer.

Assignment links
sales_data.csv
"""
# import necessary pandas library
import pandas as pd

# Step 1: Load the data from the Excel file into a Pandas DataFrame
file_path = '../sales_data.xlsx'
df = pd.read_excel(file_path)

# Step 2: Display the first 5 rows of the DataFrame to understand its structure
print("First 5 rows of the dataset:")
print(df.head())

# Step 3: Check for missing values in each column
missing_values = df.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)

# If there are missing values, decide how to handle them. For example:
# df = df.dropna()  # Drop rows with any missing values
# OR
# df.fillna(method='ffill', inplace=True)  # Forward fill missing values

# Step 4: Determine the number of unique products in the dataset
unique_products = df['Product'].nunique()
print(f"\nNumber of unique products: {unique_products}")

# Step 5: Calculate total sales (Price * Quantity) for each transaction
df['Total Sales'] = df['Price'] * df['Quantity']
print("\nDataFrame after adding the 'Total Sales' column:")
print(df.head())

# Step 6: Calculate overall sales for each product
product_sales = df.groupby('Product')['Total Sales'].sum().sort_values(ascending=False)
print("\nOverall sales for each product:")
print(product_sales)

# Step 7: Find the best-selling product (product with the highest total sales)
best_selling_product = product_sales.idxmax()
print(f"\nBest-selling product: {best_selling_product}")

# Step 8: Convert the Date column to a Pandas datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Step 9: Extract Year, Month, and Day from the Date column
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
print("\nDataFrame after adding 'Year', 'Month', and 'Day' columns:")
print(df.head())

# Step 10: Calculate total sales for each year and month
monthly_sales = df.groupby(['Year', 'Month'])['Total Sales'].sum().reset_index()
print("\nTotal sales for each year and month:")
print(monthly_sales)

# Step 11: Identify the month with the highest sales
max_sales_month = monthly_sales.loc[monthly_sales['Total Sales'].idxmax()]
print(f"\nMonth with the highest sales: {max_sales_month['Month']}, Year: {max_sales_month['Year']}")

# Step 12: Determine the number of unique customers in the dataset
unique_customers = df['Customer ID'].nunique()
print(f"\nNumber of unique customers: {unique_customers}")

# Step 13: Calculate the average purchase amount per customer
avg_purchase_per_customer = df.groupby('Customer ID')['Total Sales'].sum().mean()
print(f"\nAverage purchase amount per customer: {avg_purchase_per_customer}")


