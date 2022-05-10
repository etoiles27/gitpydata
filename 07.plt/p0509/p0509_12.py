import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import re

# item_name당 주문 개수(order_id)와 총량(합계, quantity)을 출력하시오.
# 2. 막대그래프로 표현하시오. ( title : 주문량 그래프 ylabel : 주문량, xlabel:주문번호 )

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False

# df= pd.read_csv("chipotle.txt", sep="\t", header=None)
# df.to_excel('chipotle.xlsx')
df = pd.read_excel('chipotle.xlsx',skiprows=1)

# 주문 - order id
# 수량 - quantity 

# print(df.groupby('item_name').mean())
# print(df.groupby('item_name').count())

# df['order_id']=df['order_id'].astype(str)
# print(df.groupby('order_id').count())

# print(df['order_id'].unique())

# 가장 많이 주문한 -> value_count() -> 자동 역순정렬

item_count = df['item_name'].value_counts()[:10]
print(item_count)


for i,(item_n, cnt) in enumerate(item_count.iteritems()):
    print('주문{} :'.format(i),item_n,cnt)
    
order_count = df.groupby('item_name')['order_id'].count()


