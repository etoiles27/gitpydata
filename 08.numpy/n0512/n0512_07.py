import numpy as np

# 배열합치기
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr3 = np.concatenate([arr1, arr2])

print(arr3)