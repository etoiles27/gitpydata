import numpy as np

# list1 =[9,2,7,5,6,8,1,4,3,0]
# arr = np.array(list1)

# arr.sort()
# print(arr)
# arr2 =arr[::-1] 
# print(arr2)


list2 = [[5,9,10,3,1],[8,3,4,2,5]]
arr = np.array(list2)

print(arr)
# arr.sort(axis=0)
arr.sort(axis=1)

print(arr)