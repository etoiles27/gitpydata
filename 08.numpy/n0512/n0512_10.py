import numpy as np

# lst = [[1,2,3],[4,5,6],[7,8,9]]
# arr = np.array(lst)
# arr2=arr[0:2]
# arr3=arr[0:2,0:2]
# arr4 = arr[1:,1:]
# arr5 = arr[0:,0:2]

# print(arr)
# print(arr2)
# print(arr3)
# print(arr4)
# print(arr5)

# # 1- 50. (5,10) 행렬 출력

# arr = np.arange(1,51).reshape(5,-1)
# print(arr)

# # 행3-4 열 5-9 출력
# arr1 = arr[3:5,5:10]
# print(arr1)

# arr3 = np.arange(50)
# print(arr3)
# print(arr3[3:10])


list1 =[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
arr = np.array(list1)
arr1 = np.arange(1,13).reshape(3,4)

print(arr[0,1])
idx1 = arr[[0,2],[1,3]]
idx = arr[[0,1,2],[1,2,3]]

print(idx)
