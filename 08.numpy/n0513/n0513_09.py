import numpy as np

# arr1 = np.array([[1,3],[2,4]])
# arr2 = np.array([2,5])

# result_arr =  np.dot(arr1,arr2)

# print(arr1)
# print(arr2)
# print(result_arr)

# arr3 = np.array([[5,2,3],[1,2,4],[3,2,1]])
# arr4 = np.array([4,2,1])
# arr5 = np.dot(arr3,arr4)

# print(arr5)

# arr1 = np.random.randint(1,10,(5,3))
# arr2 = np.array([4,2,1])
# arr3 = np.dot(arr1,arr2)
# print(arr1)
# print(arr2)
# print(arr3)


arr1 = np.array([[1,1],[0,1]])
arr2 = np.array([[2,0],[3,4]])

arr3 = arr1*arr2
arr4 = np.dot(arr1,arr2)

print(arr3)
print(arr4)



arr5 = np.arange(1,7).reshape(2,3)
arr6 = np.arange(7,13).reshape(3,2)
arr7 = np.dot(arr5,arr6)
print(arr7)

arr8 = np.arange(1,10).reshape(3,3)
arr9 = np.array([1,2,3])
# arr10= np.dot(arr8,arr9)
print(arr8)
# print(arr10)
arr10 = arr8*arr9
print(arr10)

arr8[1]=arr8[1]*2
arr8[2]=arr8[2]*3

print(arr8)

