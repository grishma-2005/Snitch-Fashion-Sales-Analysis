#Create Database
CREATE DATABASE stitch_fashion;

#Create Table
USE stitch_fashion;
CREATE TABLE sales_data (
    Order_ID INT,
    Customer_Name VARCHAR(100),
    Product_Category VARCHAR(50),
    Product_Name VARCHAR(100),
    Units_Sold INT,
    Unit_Price DECIMAL(10,2),
    Discount DECIMAL(5,2),
    Sales_Amount DECIMAL(12,2),
    Order_Date DATE,
    City VARCHAR(50),
    Segment VARCHAR(50),
    Profit DECIMAL(12,2)
);

#Verify Data
SELECT * FROM sales_data LIMIT 10;

#Total Sales by City
SELECT City, SUM(Sales_Amount) AS Total_Sales
FROM sales_data
GROUP BY City
ORDER BY Total_Sales DESC;

#Top Selling Product Category
SELECT Product_Category, SUM(Sales_Amount) AS Total_Sales
FROM sales_data
GROUP BY Product_Category
ORDER BY Total_Sales DESC;

#Monthly Sales Trend
SELECT 
    DATE_FORMAT(Order_Date, '%Y-%m') AS Month,
    SUM(Sales_Amount) AS Monthly_Sales
FROM sales_data
GROUP BY Month
ORDER BY Month;

#Most Profitable City
SELECT City, SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY City
ORDER BY Total_Profit DESC;

#High vs Low Discount Impact
SELECT
    City,
    CASE
        WHEN `Discount` >= 0.5 THEN 'High Discount'
        ELSE 'Low Discount'
    END AS Discount_Level,
    COUNT(Order_ID) AS Total_Orders,
    SUM(Sales_Amount) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    ROUND(AVG(`Discount`) * 100, 2) AS Avg_Discount_Percent
FROM sales_data
GROUP BY City, Discount_Level
ORDER BY City, Total_Sales DESC;

#Franchise Ranking (City Performance Ranking)
SELECT
    City,
    SUM(Sales_Amount) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    RANK() OVER (ORDER BY SUM(Sales_Amount) DESC) AS Sales_Rank
FROM sales_data
GROUP BY City
ORDER BY Sales_Rank;