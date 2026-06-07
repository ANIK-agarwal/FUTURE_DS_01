import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2️⃣ Load Dataset (replace with your dataset path)
# Example: Superstore dataset
df = pd.read_csv("archive.csv")

# 3️⃣ Quick Data Check
print("Dataset Shape:", df.shape)
print("Missing Values:\n", df.isnull().sum())

# 4️⃣ Data Cleaning
# Drop rows with missing Sales/Profit values
df = df.dropna(subset=["Sales", "Profit"])

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# 5️⃣ Revenue Trends Over Time
df["YearMonth"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("YearMonth")["Sales"].sum()

plt.figure(figsize=(12,6))
monthly_sales.plot(kind="line", marker="o")
plt.title("Revenue Trends Over Time")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()

# 6️⃣ Top-Selling Products
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=top_products.values, y=top_products.index, palette="Blues_r")
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.show()

# 7️⃣ Category & Region Analysis
category_sales = df.groupby("Category")["Sales"].sum()
region_profit = df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(12,5))
sns.barplot(x=category_sales.index, y=category_sales.values, palette="Set2")
plt.title("Sales by Category")
plt.show()

plt.figure(figsize=(12,5))
sns.barplot(x=region_profit.index, y=region_profit.values, palette="Set1")
plt.title("Profit by Region")
plt.show()

# 8️⃣ Insights & Recommendations
print("\n📌 Business Insights:")
print("- Products generating most revenue:", top_products.index[0])
print("- Most profitable region:", region_profit.idxmax())
print("- Category with highest sales:", category_sales.idxmax())

print("\n✅ Recommendations:")
print("1. Focus marketing on top-selling products to maximize revenue.")
print("2. Expand operations in", region_profit.idxmax(), "region for higher profitability.")
print("3. Invest in", category_sales.idxmax(), "category to sustain growth.")
