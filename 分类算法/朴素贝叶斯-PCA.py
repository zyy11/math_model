import matplotlib.pyplot as plt

from sklearn import datasets, metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA

iris = datasets.load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

PCA_model=PCA(n_components=2)
X_reduced = PCA_model.fit_transform(X_train)

model=GaussianNB()

model.fit(X_reduced, y_train)

_, ax = plt.subplots()

X0, X1 = X_reduced[:, 0], X_reduced[:, 1]

disp = DecisionBoundaryDisplay.from_estimator(
    model,
    X_reduced,
    response_method="predict",
    cmap=plt.cm.coolwarm,
    alpha=0.8,
    ax=ax,
    xlabel=iris.feature_names[0],
    ylabel=iris.feature_names[1],
)
ax.scatter(X0, X1, c=y_train, cmap=plt.cm.coolwarm, s=20, edgecolors="k")
ax.set_xticks(())
ax.set_yticks(())
plt.show()

X_test_PCA=PCA_model.transform(X_test)
y_pred=model.predict(X_test_PCA)
print(metrics.classification_report(y_test,y_pred))
