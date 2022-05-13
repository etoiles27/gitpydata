import numpy as np

# arr = np.arange(9).reshape(3,3)
# bol_arr = arr>5

# print(bol_arr)

# list1 = [[1,2,3],[4,5,6],[7,8,9]]
# arr1 = np.array(list1)

# idx_list = [[False,True,False],[True,True,False],[False,False,True]]
# idx = np.array(idx_list)
# print(arr1[idx])


arr1 = np.random.randint(1,100,(5,10))

idx = np.where(arr1%2==0)
print(arr1[idx])

arr2 = np.where(arr1%2==0,arr1*10,arr1*2)
print(arr2)

arr3=np.where(arr1>50,arr1,100)
print(arr3)