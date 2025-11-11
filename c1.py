import pandas as pd

# Creating a Series
list = [1, 6, 9]
Series = pd.Series(list)
print(f"Pandas Series: \n{Series}")

# Create Lables
list = [3, 8, 7]
Series = pd.Series(list, index = ['a', 'b', 'c'])
print(f"Custom labels: {Series}")