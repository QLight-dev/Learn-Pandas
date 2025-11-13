import pandas as pd

df = pd.read_csv("src/cleaning_data.csv")
# Replacing values
df.loc[7, "Duration"] = 45
print(f"Replacing row 7: \n{df.to_string}")

# Removing Rows
for i in df.index:
    if df.loc[i, "Duration"] > 120:
        df.drop(i, inplace = True)
print(f"Remove all rows that are bigger than 120: \n{df.to_string}")
