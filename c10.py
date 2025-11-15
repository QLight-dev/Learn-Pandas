import pandas as pd 

df = pd.read_csv("src/c10.csv")
# Finding Relationships
print(f"Finding relationships between columns: {df.corr()}")
