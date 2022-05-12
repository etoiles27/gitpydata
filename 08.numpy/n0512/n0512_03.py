import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False

# list_data=[0,1,2,3,4]
# arr = np.array(list_data)
# print(arr)
# arr = np.array(list_data,dtype=str)
# print(arr)
arr1 = np.arange(1,11)
print(arr1)
arr = np.linspace(1,11,4)
print(arr)
arr3 = np.linspace(0,100)
print(arr3)

arr2 = np.linspace(0,10,5, retstep=True)
print(arr2)