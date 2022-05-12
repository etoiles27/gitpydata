import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False


# 3-9 1차원 배열 생성후, 첫번째 요소 출력

arr1 = np.arange(3,10)
print(arr1[0])

#  배열 5,5 생성, 1값으로 

arr2 = np.ones((5,5))
print(arr2)

# 4,2,1,5,2,6,1,1,1, 을 (3,3)배경로 출력. 
list_data = [4,2,1,5,2,6,1,1,1]
arr3 = np.array(list_data)
print(arr3.reshape(3,3))
arr6 = np.array([list_data[0:3],list_data[3:6],list_data[6:9]])
print(arr6)
#0-30 2씩
arr4 = np.arange(0,31,2)
print(arr4)

# 0-4까지 9개의 수 균일한 간격
arr5 = np.linspace(0,4,9)
print(arr5)
