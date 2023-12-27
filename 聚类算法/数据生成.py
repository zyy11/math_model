# 综合分类数据集
import json
import numpy as np
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
import seaborn as sns

# 定义数据集
X, y = make_classification(n_samples = 1000
                           ,n_features = 2
                           ,n_informative = 2
                           ,n_redundant = 0
                           ,n_clusters_per_class = 1
                           ,flip_y = 0
                           ,class_sep = 1.5
                           ,random_state = 7
                           ,n_classes=3
                           )

np.save("X.npy",X)
np.save("y.npy",y)

plt.style.use('fivethirtyeight')

plt.figure(figsize = (10,6))
sns.scatterplot(x = X[:,0], y = X[:,1], hue = y, s = 50)
plt.show()