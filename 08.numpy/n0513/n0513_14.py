import numpy as np

# np.save -> 저장
# np.load -> 읽어오기

# arr = np.arange(10)
# np.save('np1.npy',arr)

# read_arr= np.load('np1.npy')
# print(read_arr)


# arr1 = np.arange(10)
# arr2 = np.arange(10,21)

# np.savez('np.npz',a1=arr1, a2=arr2)

r_arr = np.load('np.npz')

print(r_arr['a1'])
print(r_arr['a2'])