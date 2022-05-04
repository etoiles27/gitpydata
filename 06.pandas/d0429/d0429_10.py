import pandas as pd

df = pd.read_excel('user.xlsx')

print(df['first_name'].str.lower())
print(df['first_name'].str.contains('de',case=False))



filt1 = df['gender'].str.contains('male',case=False)
print(df[filt1])
listlan= ['female','male']
filt2 = df['gender'].str.lower().isin(listlan)
print(df[filt2])
print(len(df[filt1]))
print(len(df[filt2]))


filt3 = df['email'].str.endswith('.com')
print(df[filt3])


filt4 = df['email'].str.find('a',2)
print(filt4)
print(df[filt4==2])


filt5 = df['email'].str[2].isin(['a'])
print(df[filt5])


print(len(df[filt4==2]), len(df[filt5]))




filt10 = df['email'].str.find('@')
print(filt10)

filt11 = df['email'].str.find('.')
print(filt11)


maillist = []
for i in range(len(filt10)):
    filt12 = df['email'][i][filt10[i]:filt11[i]]
    maillist.append(filt12)
    # print(filt12)


print(maillist)



# print(df.columns)
df.insert(5,'mail',maillist)
print( df['mail'])





