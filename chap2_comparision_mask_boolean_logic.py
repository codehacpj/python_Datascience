import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set() #set plot styles

rainfall = pd.read_csv('Seattle2014.csv')['PRCP'].values
inches = rainfall/254

plt.hist(inches,40)
plt.show()
