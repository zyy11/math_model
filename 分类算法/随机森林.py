import matplotlib.pyplot as plt
from sklearn import datasets, metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model=RandomForestClassifier(n_estimators=10)

model.fit(X_train, y_train)

y_pred=model.predict(X_test)

print(metrics.classification_report(y_test,y_pred))

