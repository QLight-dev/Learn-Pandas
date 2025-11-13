import pandas as pd

df = pd.read_csv("src/cleaning_data.csv")
df["Date"] = pd.to_datetime(df["Date"], format="mixed")
print(f"Fix row 26 but not 22: \n{df.to_string}")

# ...
