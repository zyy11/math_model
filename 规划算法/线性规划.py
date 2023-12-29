from scipy.optimize import linprog

c=[-15.48,-12.53,-0.28,-28.72]
#A_ub = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
#b_ub = [15/26.14,15/22.67,15/18.76,15/30.74]
A_ub=[[26.14**2,22.67**2,18.76**2,30.74**2]]
b_ub=[25**2]
A_eq = [[1,1,1,1]]
b_eq = [1]
bounds = [(0, 1),(0, 1),(0, 1),(0, 1)]

res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)

print(res)