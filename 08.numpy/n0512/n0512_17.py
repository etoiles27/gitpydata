import numpy as np

arr1 = np.ones([3,5])
print(arr1)
arr2 = np.random.randint(1,10,(3,2))
print(arr2)


# 열 기준으로 행렬 합치기.
arr3 = np.concatenate([arr1,arr2],axis=1)
print(arr3)

# 열 기준으로 (3,4)(3,3)

left,right = np.split(arr3,[4],axis=1)
print(left)
print(right)

# 행기준으로
top,bottom = np.split(arr3,[2],axis=0)
print(top)
print(bottom)