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

# print(df)


# print(df.columns)
# print(df.sort_values(['item_name'],ascending=[False]))
# df['item_price'] = re.sub(r'$','',df['item_price'])
df['item_price']=df['item_price'].str.replace('$','').astype(float)


print(df)

# print(df.groupby('item_name').count())
# print(df.groupby('item_name')['quantity'].count())
# print(df.groupby('item_name').sum())
# print(df.groupby('item_name')['quantity'].sum())

df_cnt = df.groupby('item_name')['quantity'].count()
df_sum = df.groupby('item_name')['quantity'].sum()
# df_price = df.groupby('item_name')['item_price'].sum()

# print(df.groupby('item_name').describe())
# print(df.groupby('order_id').describe())

# print(df.groupby('order_id')['item_price'].mean())

# filt = df['order_id']==1834

# print(df.loc[filt])

# print(df.groupby('order_id').describe())

print(df.groupby('item_name')['quantity'].sum().sort_values(ascending=False).head(5))

print(df.groupby('item_name')['order_id'].count())
print(df.groupby('item_name')['quantity'].sum())
print(df.groupby('order_id')['item_price'].mean())
print(df.groupby('order_id')['item_price'].sum().mean())


# print(df_cnt.sort_values())
# 


# print('-'*100)
df_new = pd.DataFrame(df.groupby(['item_name'])['quantity'].sum())
# df_new = df.groupby('item_name')['quantity'].sum()
# df_new['cnt']=df.groupby('item_name')['quantity'].sum()
x=df_new.index
y=df_new['quantity']


plt.figure(figsize=(20,5))
plt.bar(x,y,label='주문량')
plt.title('주문량 그래프')
plt.xlabel('주문번호')
plt.ylabel('주문량')

for i, txt in enumerate(y):
    plt.text(i,txt+2,txt,ha='center')

plt.xticks(rotation = 270)
plt.legend()
plt.show()