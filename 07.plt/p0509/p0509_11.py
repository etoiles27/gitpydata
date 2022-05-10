import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import re

# item_name당 주문 개수(order_id)와 총량(합계, quantity)을 출력하시오.
# 2. 막대그래프로 표현하시오. ( title : 주문량 그래프 ylabel : 주문량, xlabel:주문번호 )

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False

# df = pd.read_excel('chipotle.xlsx',skiprows=1)

df = pd.read_excel('score.xlsx')

print(df.groupby('학교').mean())
print(df.groupby('학교')['키'].mean())
print(df.groupby('학교')['키'].mean().shape)
print(df.groupby('학교')['국어'].sum())
print(df.groupby('학교')['국어'].count())