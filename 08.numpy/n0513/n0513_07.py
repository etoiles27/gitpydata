import numpy as np

# arr1 = np.arange(6).reshape(2,3)
# arr2 = np.arange(3)
# arr3 = arr1+arr2

arr1 = np.arange(4).reshape(2,2)
arr2 = np.arange(2).reshape(1,2)

idx3 = np.multiply(arr1,arr2)
print(idx3)
idx4 = np.divide(arr1,arr2)
print(idx4)

idx5 = np.power(2,5)
print(idx5)

idx6 = np.sqrt(2)
print(idx6)

idx7 = np.sqrt(4)
print(idx7)