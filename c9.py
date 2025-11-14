import pandas as pd

df = pd.read_csv("src/cleaning_data.csv")

# Discovering duplicates
print(f"Checking if we have duplicates: \n{df.duplicated()}")

# Removing Duplicates
df.drop_duplicates(inplace = True)

