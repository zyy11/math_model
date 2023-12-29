from scipy.optimize import LinearConstraint,milp,Bounds
import numpy as np

c = -np.array([540,200,180,350,60,150,280,450,320,120])
A = [[6,3,4,5,1,2,3,5,4,2]]
b_l=[0]
b_u=[30]
integrality = np.ones_like(c)
constraints = LinearConstraint(A, b_l, b_u)
bounds=Bounds(lb=0,ub=1)

res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)
print(res)