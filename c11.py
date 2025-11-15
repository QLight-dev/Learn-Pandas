import pandas as pd 
import matplotlib 
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 

df = pd.read_csv("src/c11.csv")

# Visualize full DataFrame
df.plot()
print("Showing full view of DataFrame...")
plt.show()
print("Full DataFrame view closed.")

# Scatter plot
df.plot(kind = "scatter", x = "Duration", y = "Calories")
print("Showing Scatter plot....")
plt.show()
print("Scatter plot closed.")

# Histogram
df["Duration"].plot(kind = "hist")
print("Showing Histogram...")
plt.show()
print("Histogram closed.")