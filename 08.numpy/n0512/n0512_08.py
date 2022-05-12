import numpy as np

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])

# arr3 = np.concatenate([arr1, arr2])

# arr4 = arr3.reshape((2,3))

# print(arr4)

# arr1 = np.arange(1,10)
# arr2 = arr1.reshape((3,3))

# arr3 = np.arange(1,11).reshape((2,5))
# arr4 = np.arange(20).reshape((4,5))
# arr5 = np.linspace(1,20,10).reshape((5,2))
# print(arr5)

# arr1 = np.arange(12).reshape((3,4))
# arr = np.arange(12).reshape(4,-1)
arr1 = np.arange(12)
arr2 = np.arange(15)

# arr3 = arr1.reshape(3,-1)
# arr4 = arr2.reshape(3,-1)
arr3 = arr1.reshape(-1,6)
arr4 = arr2.reshape(-1,3)
print(arr3)
print(arr4)