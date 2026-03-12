import pandas as pd
data = {
    "Product": ["Laptop","Phone","Laptop","Tablet","Phone","Laptop","Tablet"],
    "Month": ["Jan","Jan","Feb","Feb","Mar","Mar","Mar"],
    "Units_Sold": [5,10,3,7,8,6,4],
    "Price": [800,500,800,300,500,800,300]
}
df = pd.DataFrame(data)
print("Sales Dataset")
print(df)

df["Revenue"] = df["Units_Sold"] * df["Price"]
print("\nRevenue Data")
print(df)

Total_sales = df["Revenue"].sum()
print("\nTotal Revenue:", Total_sales)

Best_product = df.groupby("Product")["Units_Sold"].sum()
print("\nUnits Sold per Product")
print(Best_product)

Monthly_Sales = df.groupby("Month")["Revenue"].sum()
print("\nMonthly Revenue")
print(Monthly_Sales)

df.to_csv("sales_results.csv", index=False)

print("\nFile saved as sales_results.csv")
