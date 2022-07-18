import numpy as np
import pandas as pd
import re


df=pd.read_csv('10.mlearn/m0711/train.csv')
print(df['level'].value_counts())

dup =df.drop_duplicates(['full_log'], keep='first', inplace=False, ignore_index=False)
print(dup['level'].value_counts())