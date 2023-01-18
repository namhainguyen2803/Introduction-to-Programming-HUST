import numpy as np

def system_solver(a):
    row = np.shape(a)[0]
    A = []
    B = []
    for i in range(row):
        A.append(a[i][:row])
        B.append(a[i][row])
    A = np.array(A)
    B = np.array(B)
    res = np.matmul(np.linalg.inv(A),B)
    res = np.array(res).reshape(-1,1)
    return res
a = np.array([[1, 3, -2, 5], 
	      [3, 5, 6, 7], 
	      [2, 4, 3, 8]])
print(system_solver(a))