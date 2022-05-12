import numpy as np

# where

# arr = np.arange(4,15)
# print(arr)
# arr2 = arr.reshape(2,-1)
# print(arr2)
# arr3 = np.arange(20).reshape(4,-1)
# print(arr3)

# arr4 = arr3.reshape(2,5,-1)
# print(arr4)


# a1 = np.where(arr%2==0)
# print(a1)

# print(arr[a1])


# arr1 = np.random.randint(1,10,20)
# print(arr[np.where(arr%2==0)])
# arr2 = np.arange(1,20)
# idx = np.where(arr2>10)
# print(arr2[idx])


# arr = np.arange(10).reshape(2,-1)
# print(arr)
# idx = np.where(arr%2==0)
# print(arr[idx])


# arr = np.arange(20).reshape(4,5)
# arr = np.array([2,5,1,3,0,6,5,4,7,2,9])
# print(arr)
# idx = np.where(arr>3)
# print(arr[idx])

# arr = np.arange(20)
# idx = np.where(arr%3==0,arr,0)
# idx2 = np.where(arr<10,arr,19)
# print(arr[idx])
# print(arr[idx2])


arr = np.arange(20)
arr2=arr.reshape(2,5,2)
a1 = np.arange(10).reshape(5,2)
a2 = np.arange(10,20).reshape(5,2)
print(arr2)
print(a1)
print(a2)