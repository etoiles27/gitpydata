import numpy as np

# 0-7 1차원 행렬 ->(2,4) 2차원 행렬로 변경 ->(2,2) 3차원행렬로 변경

arr1 = np.arange(8).reshape(2,4)
print(arr1)
a = arr1.reshape(2,2,2)
print(arr1.reshape(2,2,2))
print(a[1,0,0])
print(a[0][1,1])
print(a[1][1,0])
print('-'*10)
#1-4 (2,2) 행렬생성, 2값 출력 -> 2차원 행렬을 1차원 행렬로 변경

arr2 = np.arange(1,5).reshape(2,2)
print(arr2[0,1])
# print(np.concatenate(arr2))
# print(arr2.reshape(4))
print(arr2.flatten())

print('-'*10)

# 15,8,12,11,7,3 (2,3) 행렬 -> 10보다 큰수가 몇개인지 출력
lst = [15,8,12,11,7,3]

arr3 = np.array(lst).reshape(2,3)
print(arr3)

idx = np.where(arr3>10)

print(len(arr3[idx]))
print(arr3[idx].size)