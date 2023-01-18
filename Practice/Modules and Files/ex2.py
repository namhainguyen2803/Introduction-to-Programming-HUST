import numpy as np

def convert(a):
    row, col = np.shape(a)
    res = []
    for i in range(row):
        for j in range(col):
            sub = a[i][j]/sum(a[i])
            res.append(sub)
    res = np.array(res)
    return res.reshape(row,col)
print(convert(np.arange(0, 9).reshape(3, 3)))
    