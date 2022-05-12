import numpy as np



# # 1차원 행렬
# arr1 = np.arange(10)
# arr2 = np.arange(10,20)

# arr3 = np.concatenate([arr1,arr2],axis=0)
# print(arr3)

# 2차원 행렬

# arr1 = np.arange(4).reshape(1,-1)

# print(arr1)
# arr2 = np.arange(8).reshape(2,-1)
# print(arr2)

# arr3 = np.concatenate([arr1, arr2],axis=0)

# print(arr3)


arr1 = np.arange(4).reshape(2,-1)
arr2 = np.arange(4,8).reshape(2,-1)
arr3 = np.concatenate([arr1, arr2],axis=1)
print(arr3)