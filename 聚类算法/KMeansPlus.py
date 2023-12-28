import numpy as np
from sklearn import cluster,metrics
import matplotlib.pyplot as plt
import seaborn as sns

X=np.load("X.npy")
y=np.load("y.npy")

two_means = cluster.KMeans(
        n_clusters=4,
        init='k-means++',
        n_init="auto"
    )

two_means.fit(X)
y_pred = two_means.predict(X)

#plt.style.use('fivethirtyeight')

print(metrics.rand_score(y,y_pred))

plt.figure(figsize = (10,6))
sns.scatterplot(x = X[:,0], y = X[:,1], hue = y_pred, s = 50)
plt.show()

