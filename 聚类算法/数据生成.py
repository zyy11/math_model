# 综合分类数据集
import numpy as np
from sklearn.datasets import make_classification


# 定义数据集
X, y = make_classification(n_samples = 1000
                           ,n_features = 2
                           ,n_informative = 2
                           ,n_redundant = 0
                           ,n_clusters_per_class = 1
                           ,flip_y = 0
                           ,class_sep = 2
                           ,random_state = 7
                           ,n_classes=4
                           )

np.save("X.npy",X)
np.save("y.npy",y)


