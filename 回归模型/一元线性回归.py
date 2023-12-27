import sklearn
from statsmodels.formula.api import ols
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

data=pd.read_csv("crime.csv")
#print(data)
linear_model = ols('crime ~ unemployment',data=data).fit()

print(linear_model.summary())

  # modify figure size

fig = plt.figure(figsize=(14, 8))

fig = sm.graphics.plot_regress_exog(linear_model,'unemployment',fig=fig)

plt.show()
