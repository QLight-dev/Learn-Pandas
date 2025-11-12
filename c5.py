import pandas as pd
# viewing the data
df = pd.read_csv("src/c5.csv")
print(f"Print 10 lines of DataFrame: \n{df.head(10)}")
print(f"Print 5 lines of DataFrame (without specification): \n{df.head()}")
print(f"Print the last 10 lines of DataFrame: \n{df.tail(10)}")

# Print info about the data
print(df.info())