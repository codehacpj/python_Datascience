import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("president_heights.csv")
heights = np.array(data["height(cm)"])
print (heights)

print("Mean height: ",np.mean(heights))
plt.hist(heights,Title="Normal distribution of heights of presidents")

plt.show()

