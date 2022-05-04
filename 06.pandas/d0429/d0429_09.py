import pandas as pd


df = pd.read_excel('user.xlsx')


# cond1 = df['first_name'].str.startswith('De') | df['last_name'].str.startswith('De')
cond2 = df['first_name'].str.contains('de')  | df['last_name'].str.contains('de') \
    | df['first_name'].str.contains('De')  | df['last_name'].str.contains('De')
    

print(df[cond2])
langs=['de','De']
cond3 = df['first_name'].str.contains('de', case=False) |df['last_name'].str.contains('de',case=False)

print(df[cond3])





df = pd.read_excel('score.xlsx')
cond4 = df['SW특기'].str.contains('python', case=False, na=False)
print(df[cond4])
# lanlist = ['python', 'java']
# print(df[cond4.str.lower().isin(lanlist)])