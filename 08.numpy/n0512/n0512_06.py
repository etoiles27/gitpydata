import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False


# random
# numpy 행렬, 일률적으로 숫자를 입력해서 행렬

arr1 = np.random.randint(0,10,(3,3))
arr2 = np.random.rand(8)
arr = np.random.normal(0,1,(3,3))
print(arr)

