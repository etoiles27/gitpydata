import numpy as np


# 행렬 합치기 -> np.concatenate
# 행렬 나누기 -> np.split

arr = np.arange(8).reshape(2,4)
print(arr)
left, right = np.split(arr,[2],axis=1)
print(left)
print(right)

left, right = np.split(arr,[1],axis=1)
print(left)
print(right)


top, bottom = np.split(arr,[1],axis=0)
print(top)
print(bottom)
