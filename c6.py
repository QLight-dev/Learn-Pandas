import pandas as pd

df = pd.read_csv("src/cleaning_data.csv")

# return a new DataFrame without any empty cells
new_df = pd.dropna(df)
print(f"Old DataFrame (with empty cells): {df}")
print(f"New DataFrame (without empty cells): ")