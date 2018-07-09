import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set()   ## For the plot style

data = pd.read_csv('president_heights.csv')

heights = np.array(data['height(cm)'])

plt.hist(heights)
plt.title('Height Distribution of the US presidents')
plt.xlabel('height(cm)')
plt.ylabel('number')
plt.show()
