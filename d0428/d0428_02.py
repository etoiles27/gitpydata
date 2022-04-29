import pandas as pd


arr = [-20,-10,10,20]
temp = pd.Series(arr,index=['Jan','Feb','Mar','Apr'])

print(temp)


# index로 출력
print(temp['Jan'])