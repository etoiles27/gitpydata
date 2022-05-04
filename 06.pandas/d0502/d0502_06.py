import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')



# df.loc['7번','키'] = 190
# df.loc['7번','키':'영어'] = [190,100,100]
# df.loc['7번',['국어','영어']] = [100,100]
# df.loc['9번']=['이순신','디지털고',200,100,100,70,90,80,'java']

# df.loc['4번','SW특기'] = 'python'

# df.loc[['4번','5번'],'SW특기'] = 'python'
# df.loc['4번',['키','국어']]=[200,100]



# 컬럼 순서 변경 

df['총합'] = df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
df['결과'] = '불합격'
df.loc[df['총합']>400,'결과'] ='합격' 
print(df)



# cols = ['이름','학교','총합','결과']
cols = list(df.columns)
df = df[cols[0:2] + [cols[-1]] + [cols[-2]] + cols[2:9]]
print(df)