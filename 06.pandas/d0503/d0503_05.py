import pandas as pd

# data1 = pd.read_csv('2020년연봉.csv',encoding='utf-8-sig')
# data2 = pd.read_csv('2021년연봉.csv',encoding='utf-8-sig')
# data3 = pd.read_csv('2022년연봉.csv',encoding='utf-8-sig')

# # print(data1.groupby('팀').mean())

# df = pd.concat([data1, data2, data3])

# df.to_csv('전체연봉.csv',encoding='utf-8-sig',index=False)


df = pd.read_csv('전체연봉.csv',encoding='utf-8-sig')

print(df)
