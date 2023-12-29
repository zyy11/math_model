from scipy.optimize import minimize
import numpy as np

fx=lambda x:-(15.48*x[0]+12.53*x[1]+0.28*x[2]+28.72*x[3]-3)/(26.14**2*x[0]+22.67**2*x[1]+18.76**2*x[2]+30.74**2*x[3])**0.5
cons=({'type':'eq', 'fun':lambda x:sum(x)-1},
      {'type':'ineq', 'fun':lambda x:min(x)})

res=minimize(fx,np.array([0,0,0,1]),constraints=cons,method='SLSQP')
print(res)