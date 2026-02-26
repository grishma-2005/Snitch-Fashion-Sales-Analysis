import pandas as pd
import numpy as np

df = pd.read_excel("Snitch_Fashion_Sales_Uncleaned.xlsx")

# Clean City
df['City'] = df['City'].astype(str).str.strip().str.title()

city_map = {
    'Bengaluru': 'Bangalore',
    'Hyd': 'Hyderabad',
    'Hyderbad': 'Hyderabad'
}

df['City'] = df['City'].replace(city_map)

# Fix Units_Sold
df['Units_Sold'] = pd.to_numeric(df['Units_Sold'], errors='coerce')
median_units = df.loc[df['Units_Sold'] > 0, 'Units_Sold'].median()

df.loc[df['Units_Sold'] <= 0, 'Units_Sold'] = median_units
df['Units_Sold'].fillna(median_units, inplace=True)

# Fix Discount
df['Discount_%'] = pd.to_numeric(df['Discount_%'], errors='coerce')
df.loc[df['Discount_%'] > 1, 'Discount_%'] = 1

discount_median = df['Discount_%'].median()
df['Discount_%'].fillna(discount_median, inplace=True)

# Fix Dates
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
most_common_date = df['Order_Date'].mode()[0]
df['Order_Date'].fillna(most_common_date, inplace=True)

# Recalculate Sales_Amount
df['Sales_Amount'] = df['Units_Sold'] * df['Unit_Price'] * (1 - df['Discount_%'])

# Clean Profit
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')
profit_median = df.loc[df['Profit'] > 0, 'Profit'].median()

df.loc[df['Profit'] <= 0, 'Profit'] = profit_median
df['Profit'].fillna(profit_median, inplace=True)

# Fix Unit_Price
df['Unit_Price'] = pd.to_numeric(df['Unit_Price'], errors='coerce')
price_median = df['Unit_Price'].median()
df['Unit_Price'].fillna(price_median, inplace=True)

# Save Cleaned File
df.to_csv("Snitch_Fashion_Sales_Cleaned.csv", index=False)
df.to_excel("Snitch_Fashion_Sales_Cleaned.xlsx", index=False)

print("Data Cleaning Completed Successfully")