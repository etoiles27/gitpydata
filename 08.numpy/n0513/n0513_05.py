import numpy as np

# arr1 = np.arange(1,12,2)

# data_list = [1,3,5,7,9,11]
# arr = np.array(data_list)
# arr2 = arr+3

# print(arr2)

# arr = np.array([20,30,40,50])


arr = np.random.randint(1,10,4).reshape(2,2)
print(arr)
arr = arr*10
print(arr)

arr2 = np.random.randint(1,10,25).reshape(5,5)
arr3 = np.where(arr2>5,arr2*10,arr2)
print(arr3)