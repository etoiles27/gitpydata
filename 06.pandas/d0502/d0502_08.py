import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')


print(df.columns)
# print(df.index)
# 이름    학교   결과   총합    키   국어   영어   수학  과학  사회        SW특기
# df.columns=['name','school','height','kor','eng','math','sci','soc','SW']

df.rename(columns={'이름':'name', '학교':'school'},inplace=True)

print(df)