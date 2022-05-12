import numpy as np

# arr1 = np.array([[10,20,30],[3,50,5]])
# arr2 = np.array([[70,80,90],[100,110,120]])


# idx = np.where(arr1>20,arr1,arr2)

# print(idx)



# 1- 100 
arr = np.random.randint(1,101,(10,10))
# print(arr)
idx = np.where(arr>=50)
print(arr[idx])


# 0 -20 
arr2 = np.random.randint(0,21,20)
arr3 = np.where(arr2>=10,arr2,0)
print(arr2)
print(arr3)


