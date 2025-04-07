
import pandas as pd

# Load the dataset
file_path = r'C:\Users\sujan\Downloads\python_sales_analysis\data\sales_data_sample.csv'
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Total Sales by Category
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

# Plotting
plt.figure(figsize=(8, 5))
category_sales.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('category_sales.png')  # Saves the chart

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create a 'Month' column (YYYY-MM)
df['Month'] = df['Date'].dt.to_period('M').astype(str)

# Group by Month and sum Sales
monthly_sales = df.groupby('Month')['Sales'].sum()

# Plot Monthly Sales Trend
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind='line', marker='o', color='green')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_sales_trend.png')

# Top 5 Customers by Total Sales
top_customers = df.groupby('Customer')['Sales'].sum().sort_values(ascending=False).head(5)

# Plot Top 5 Customers
plt.figure(figsize=(8, 5))
top_customers.plot(kind='bar', color='orange')
plt.title('Top 5 Customers by Sales')
plt.xlabel('Customer')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_5_customers.png')

# Exporting cleaned data to a new CSV file
df.to_csv('cleaned_sales_data.csv', index=False)
