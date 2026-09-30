import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------
# DATA SCIENCE INTERNSHIP PROJECT
# -----------------------------------

# Create sample sales dataset
data = {
    "Product": [
        "Laptop", "Mobile", "Headphones", "Keyboard",
        "Mouse", "Monitor", "Tablet", "Laptop",
        "Mobile", "Headphones"
    ],
    "Category": [
        "Electronics", "Electronics", "Accessories", "Accessories",
        "Accessories", "Electronics", "Electronics", "Electronics",
        "Electronics", "Accessories"
    ],
    "Quantity": [2, 5, 10, 8, 15, 3, 4, 1, 6, 12],
    "Price": [55000, 20000, 1500, 2500, 800, 12000, 25000, 55000, 20000, 1500],
    "Discount": [5, 10, 15, 5, 10, 8, 12, 5, 10, 15]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Calculate total sales
df["Total_Sales"] = (
    df["Quantity"] * df["Price"] * (1 - df["Discount"] / 100)
)

# -----------------------------------
# 1. DISPLAY DATA
# -----------------------------------

print("\n--- DATASET ---")
print(df)

# -----------------------------------
# 2. BASIC INFORMATION
# -----------------------------------

print("\n--- DATASET INFORMATION ---")
print(df.info())

print("\n--- STATISTICAL SUMMARY ---")
print(df.describe())

# -----------------------------------
# 3. CHECK MISSING VALUES
# -----------------------------------

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# -----------------------------------
# 4. NUMPY CALCULATIONS
# -----------------------------------

average_sales = np.mean(df["Total_Sales"])
maximum_sales = np.max(df["Total_Sales"])
minimum_sales = np.min(df["Total_Sales"])

print("\n--- NUMPY ANALYSIS ---")
print("Average Sales:", average_sales)
print("Maximum Sales:", maximum_sales)
print("Minimum Sales:", minimum_sales)

# -----------------------------------
# 5. TOP PRODUCTS
# -----------------------------------

top_products = df.sort_values(
    by="Total_Sales",
    ascending=False
)

print("\n--- TOP PRODUCTS ---")
print(top_products[["Product", "Total_Sales"]].head())

# -----------------------------------
# 6. BAR CHART
# -----------------------------------

plt.figure(figsize=(10, 5))

plt.bar(df["Product"], df["Total_Sales"])

plt.title("Product-wise Total Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# -----------------------------------
# 7. HISTOGRAM
# -----------------------------------

plt.figure(figsize=(8, 5))

plt.hist(df["Total_Sales"], bins=5)

plt.title("Distribution of Total Sales")
plt.xlabel("Total Sales")
plt.ylabel("Frequency")

plt.tight_layout()

plt.show()

# -----------------------------------
# 8. SAVE CLEANED DATASET
# -----------------------------------

df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned dataset saved successfully!")