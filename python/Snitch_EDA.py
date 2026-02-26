import pandas as pd
import matplotlib.pyplot as plt

# =============================
# Load Cleaned Dataset
# =============================

df = pd.read_excel("Snitch_Fashion_Sales_Cleaned.xlsx")

print("Dataset Loaded Successfully")
print(df.head())
print(df.info())


# =============================
# Date Handling
# =============================

df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Month'] = df['Order_Date'].dt.to_period('M')


# =============================
# Monthly Sales Trend
# =============================

monthly_sales = df.groupby('Month')['Sales_Amount'].sum()

print("\nMonthly Sales Trend:")
print(monthly_sales)

plt.figure()
monthly_sales.plot(kind='line', title='Monthly Sales Trend')
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()


# =============================
# Month-over-Month Growth %
# =============================

monthly_growth = monthly_sales.pct_change() * 100

print("\nMonth-over-Month Growth %:")
print(monthly_growth)

plt.figure()
monthly_growth.plot(kind='bar', title='Month-over-Month Growth %')
plt.xlabel("Month")
plt.ylabel("Growth %")
plt.tight_layout()
plt.show()


# =============================
# Category Performance
# =============================

category_sales = df.groupby('Product_Category')['Sales_Amount'].sum().sort_values(ascending=False)
print("\nCategory-wise Sales:\n", category_sales)
print(category_sales)

plt.figure()
category_sales.plot(kind='bar', title='Category Performance')
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()


# =============================
# City Performance
# =============================

city_sales = df.groupby('City')['Sales_Amount'].sum().sort_values(ascending=False)

print("\nCity Performance:")
print(city_sales)

plt.figure()
city_sales.plot(kind='bar', title='City Performance')
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()


# =============================
# Profit Analysis by Category
# =============================

profit_category = df.groupby('Product_Category')['Profit'].sum().sort_values(ascending=False)

print("\nProfit by Category:")
print(profit_category)

plt.figure()
profit_category.plot(kind='bar', title='Profit by Category')
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.show()


print("\nEDA + Visualization Completed Successfully")
