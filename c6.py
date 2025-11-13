import pandas as pd

df = pd.read_csv("src/cleaning_data.csv")

# return a new DataFrame without any empty cells
new_df = df.dropna()
print(f"Old DataFrame (with empty cells): \n{df.to_string}")
print(f"New DataFrame (without empty cells): \n{new_df.to_string}")

# Remove all empty cells within Original DataFrame
df.dropna(inplace = True)
print(f"Old DataFrame (without empty cells): \n{df.to_string}")

# Replace All empty cells to 100 in Calories
df = pd.read_csv("src/cleaning_data.csv")
df.fillna({"Calories": 100}, inplace = True)
print(f"All empty cells in Calories changed to 100: \n{df}")

# Replace All empty cells to the average in Calories
df = pd.read_csv("src/cleaning_data.csv")
x = df["Calories"].mean()
df.fillna({"Calories": x}, inplace = True)
print(f"Change all values in Calories to average: \n{df}")