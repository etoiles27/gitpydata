import numpy as np

# arr = np.arange(16).reshape(4,4)
# print(arr)

# print(np.max(arr))
# print(np.min(arr))
# print(np.sum(arr))
# print(np.mean(arr))

# arr = np.array([[1,2],[3,4]])

# arr_sum = np.sum(arr)
# # arr_max = np.max(arr)

# ax0_arr = np.sum(arr,axis=0)
# ax1_arr = np.sum(arr,axis=1)

# print(arr_sum,ax0_arr,ax1_arr)

arr = np.arange(1,10).reshape(3,3)
print(arr)
ax0_arr = np.sum(arr,axis=0)
ax1_arr = np.sum(arr,axis=1)
print("col sum : {}".format(ax0_arr))
print("row sum : {}".format(ax1_arr))