import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False

x = [1,2,3,4,5,6,7,8,9,10]

x1 = np.arange(1,11) 
print(list(x1))

list_data = [
    [1,2,3],
    [4,5,6]
]

print(list_data)

arr = np.array(list_data)
print(arr)
print(arr.shape)
print(arr[0,1])
arr1=np.arange(4)
print(arr1)
arr2 = np.arange(2,10)
print(arr2)
arr3 = np.arange(1,10,2)
print(arr3)
arr4 = np.arange(0,10,3)
print(arr4)