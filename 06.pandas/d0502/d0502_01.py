import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')

# print(df)


# # 데이터수정 = 데이터 1개 출력 = 값만 넣어주면 수정 
# df['학교'].replace({'구로고':'단지고','디지털고':'상생고'},inplace=True)
# df['국어'].replace({100:190},inplace=True)
# df['SW특기']=df['SW특기'].str.lower()
# # 데이터 추가 
# # 새로운 index가 입력되면 추가 
# df.loc['9번'] = ['이순신','디지털고',200,100,100,100,90,80,'python']
# df['총합'] = df['국어']+df['영어']+df['수학']+df['과학']+df['사회']

# filt = df['키']>=190
# df.loc[filt,'국어'] = 100


# df.loc['4번','SW특기'] = 'python'
# df.loc['4번',['학교','SW특기']] = ['디지털고','python']

# filt = df['국어']==40
# print(filt)

# # filt2 = df.loc[filt,'국어'][1] ==40

# # 강태원 국어 40 -> 50 으로 바꾸기
# filt3 = (df['이름'] == '강태원') & filt
# df.loc[filt3, '국어'] = 50

# # 국어 40점 다 50점으로 바꾸기
# df.loc[filt,'국어'] = 50
# df['국어'].replace({40:50},inplace=True)

# # 강태원, 국어 40점이면 영,수,과,사 모두 40점
# df.loc[filt3,['영어','수학','과학','사회']] = [40,40,40,40]



df['학교'] = df['학교'] +'등학교' 
df['키']=(df['키']).astype(str) +' cm'


print(df)
