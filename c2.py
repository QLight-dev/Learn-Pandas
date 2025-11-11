import pandas as pd

# Create a DataFrame
data = {
    "Days": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday"],
    "Temperature": [40, 37, 32, 34, 35, 41, 43]
}

df = pd.DataFrame(data)

print(f"Pandas DataFrame: \n{df}")
print(f"Accessing rows (0): \n{df.loc[0]}")
print(f"Access multiple rows (5, 6): \n{df.loc[[5, 6]]}")

# Named Indexes
data = {
    "Temperature": [40, 37, 36, 34, 35, 37, 38]
}
df = pd.DataFrame(data, index = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
print(f"Named Indexes: {df}")

# Accessing Named Indexes
print(f"Accessing Named Indexes (Tuesday): \n{df.loc["Tuesday"]}")