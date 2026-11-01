import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

file = Path(__file__).parent / 'SampleSuperstore.csv'

df = pd.read_csv(file)

print("SUPERSTORE SALES ANALYSIS")
print(df.head())

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
profit_margin = (total_profit / total_sales)* 100

print("Total Sales:", round(total_sales, 2))
print("Total Sales:", round(total_profit,2))

print("Profit_Margin:",round(profit_margin,2),"%")

print("\nREGION-WISE SALES AMALYSIS")

region_sales = df.groupby('Region')['Sales'].sum()


region_sales = region_sales.sort_values(ascending=False)

print(region_sales)

print("\nCATEGORY WISE SALES ANALYSIS")

category_sales = df.groupby('Region')['Sales'].sum()

category_sales = category_sales.sort_values(ascending=False)

print(category_sales)

print("\n TOP 10 BEST-SELLING PRODUCTS")

top_products = df.groupby('Product Name')['Sales'].sum()

top_products =  top_products.sort_values(ascending=False)

print(top_products.head(10))

print("\nMONTHLY SALES ANALYSIS")

df['Order Date'] = pd.to_datetime(df['Order Date'],format='%m/%d/%Y')

df['Month']= df['Order Date'].dt.to_period('M')

monthly_sales = df.groupby('Month')['Sales'].sum()

print(monthly_sales)

print("\nMONTHLY SALES BAR CHART")

monthly_sales.plot(kind='bar', figsize=(12,5))
plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Total sales")
plt.tight_layout()
plt.show()

print("\nREGION WISE SALES BAR CHART")

region_sales.plot(kind='bar', figsize=(8, 5))

plt.title("Region Wise Sales Analysis")
plt.xlabel("Region")
plt.ylabel("Total sales")
plt.tight_layout()
plt.show()

print("\nCATEGORY WISE SALES BAR CHART")

category_sales = df.groupby('Category')['Sales'].sum()
category_sales = category_sales.sort_values(ascending=False)

category_sales.plot(kind='bar', figsize=(8, 5))

plt.title("Category Wise Sales Analysis")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()

print("\nREGION WISE PROFIT ANALYSIS")

region_profit = df.groupby('Region')['Profit'].sum()
region_profit = region_profit.sort_values(ascending=False)

print(region_profit)

print("\nREGION WISE PROFIT BAR CHART")

region_profit.plot(kind='bar', figsize=(8, 5))
plt.title("Region Wise Profit Analysis")
plt.xlabel("Region")
plt.ylabel("Total Profit")

plt.tight_layout()
plt.show()

print("\nCATEGORY WISE PROFIT BAR ANALYSIS")
category_profit = df.groupby('Category')['Profit'].sum()

category_profit= category_profit.sort_values(ascending=False)

print(category_profit)

print("\nTOP 10 LOSS-MAKING PRODUCTS")

product_profit = df.groupby('Product Name')['Profit'].sum()

loss_product = product_profit[product_profit<0]

top_10_loss = loss_product.sort_values(ascending=True).head(10)
print(top_10_loss)


print("\nTOP 10 LOSS-MAKING PRODUCTS BAR CHART")

top_10_loss.plot(kind='bar', figsize=(12, 6))

plt.title("Top 10 Loss-Making Products")
plt.xlabel("Total Loss")
plt.ylabel("Product Name")

plt.tight_layout()
plt.show()

print("\n========== FINAL BUSINESS REPOST==========")

print("Total Sales:", round(total_sales,2))
print("Total Profit:", round(total_profit,2))
print("Profit Margin:", round(profit_margin,2), "%")

print("Best Sales Region:",region_sales.idxmax())
print("Best Sales Category:",category_sales.idxmax())
print("Moat Profitable Region:",region_profit.idxmax())
print("Moat Profitable Category:",category_profit.idxmax())

print("======================================================")

report = f"""SUPERSTORE SALES ANALYSIS REPORT

Total Sales:{total_sales:2f}
Total Profit:{total_profit:2f}
Total Mragin:{profit_margin:2f}%

Best Sales Region:{region_sales.idxmax()}
Best Sales Category:{category_sales.idxmax()}

Most Profitable Region:{region_profit.idxmax()}
Most Profitable Category:{category_profit.idxmax()}"""

with open("superstore_Report.txt", "w") as f:
    f.write(report)

print("Report saved successfully!")
