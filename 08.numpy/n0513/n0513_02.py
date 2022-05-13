import numpy as np

arr = np.arange(1,9).reshape(2,-1)
print(arr)

idx1 = np.where(arr>5)
idx = np.where(arr>5,100,0)
print(idx)
