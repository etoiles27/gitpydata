import pandas as pd


def add_cm(height):
    return str(height) + 'cm'
def capChange(word):
    return word.capitalize()
def lowerChange(word):
    return word.lower()
def add_cm2(height):
    if height>=188:
        height=str(height)+'cm'
    else:
        height=str(height)+'센티미터'
    return height

df = pd.read_excel('score.xlsx',index_col='지원번호')

df['키']=df['키'].apply(add_cm2)

# df['키']=df['키'].astype(str) + 'cm'

# 함수적용
# df['키']=df['키'].apply(add_cm)

# df.fillna('java',inplace=True)

# df['SW특기']=df['SW특기'].apply(lowerChange)



print(df)

