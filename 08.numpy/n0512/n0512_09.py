import numpy as np

# arr = np.arange(12)

# print(arr.reshape(-1,1))
# print(arr.reshape(-1,3))
# print(arr.reshape(1,-1))
# print(arr.reshape(2,-1))



#5,10의 행렬을 2의 배수로
arr = np.arange(2,101,2)
print(arr.reshape(5,10))

arr2 = np.ones(21).reshape(3,7)
print(arr2)