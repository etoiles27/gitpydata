import numpy as np

# randomn - (4,4)

# arr = np.random.randn(16).reshape(4,4)
arr = np.random.randn(4,4)
idx =np.where(arr>0,2,-2)
print(arr)
print(idx)

# 행렬2개 만들어 합치기, 1-11 홀수 (3,2) + 2-12 짝수(3,2)

arr_o = np.arange(1,12,2).reshape(3,2)
print(arr_o)
arr_e = np.arange(2,13,2).reshape(3,2)
print(arr_e)

arr2 = np.concatenate([arr_o,arr_e],axis=1)
print(arr2)

# 행렬 분리 0-99 (10,10) -> 3열 기준 2개 형렬로 분리
arr3 = np.arange(0,100).reshape(10,10)
print(arr3)

left, right = np.split(arr3,[3],axis=1)
print(left)
print(right)

top, bottom = np.split(arr3,[3],axis=0)
print(top)
print(bottom)