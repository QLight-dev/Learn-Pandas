import pandas as pd

# Pandas read csv
df = pd.read_csv("src/c3.csv")
print(f"Print part of DataFrame: \n{df}")
print(f"Print Full DataFrame (using to_string): {df.to_string()}")

# Check max_rows for Pandas
print(f"check max_rows: {pd.options.display.max_rows}")

# Change max_rows
pd.options.display.max_rows = 9999
print(f"Print full DataFrame (without to_string): {df}")