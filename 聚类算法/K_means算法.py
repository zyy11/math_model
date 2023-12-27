import numpy as np
from sklearn import cluster

X=np.load("X.npy")

two_means = cluster.MiniBatchKMeans(
        n_clusters=3,
        n_init="auto"
    )

two_means.fit(X)
y_pred = two_means.predict(X)

