import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

X=np.load("X.npy")
y=np.load("y.npy")

plt.figure(figsize = (10,6))
sns.scatterplot(x = X[:,0], y = X[:,1], hue = y, s = 50)
plt.show()