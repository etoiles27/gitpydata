import pandas as pd

df = pd.read_csv('train.csv',encoding='utf-8-sig')

# 4-1 male & pclass == 1 
# print(df.columns)
# ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
# print(df['Sex'])
# print(df['Pclass'])
filt1 = (df['Sex'] == 'male')
filt2 = (df['Pclass'] == 1)
print(df.loc[filt1 & filt2])
# print(df.loc[filt1 & filt2,'PassengerId':'Sex'])

# 4-2 survive == 1 age <=20
cond1 = (df['Survived'] == 1)
cond2 = (df['Age'] <= 20)
# print(df.loc[cond1 & cond2,'Survived':'Age'])
print(df.loc[cond1 & cond2])

# 4-3 그룹. survivied, pclass 
print('-'*20)
print(df.groupby(['Survived','Pclass']).count())
print(df.groupby(['Survived','Pclass']).describe())
