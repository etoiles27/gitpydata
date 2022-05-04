import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_excel('./score.xlsx')

print(df['지원번호'])
print(df['국어'])

x=df['지원번호']#[1,2,3]
y=df['국어']#[2,4,8]
z=df['영어']#[2,4,8]

plt.plot(x,y)
plt.plot(x,z)
plt.show()