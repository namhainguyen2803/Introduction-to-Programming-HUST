import numpy as np
a = np.arange(1, 21).reshape(4,5).reshape(5,4,order='F').T
print(a)
