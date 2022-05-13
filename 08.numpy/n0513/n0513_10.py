import numpy as np



arr1 = np.arange(8).reshape(2,4)
arr2 = np.arange(8).reshape(2,4)


arr3 = np.concatenate([arr1,arr2],axis=0)

print(arr3)

arr4 = np.arange(4).reshape(4,1)