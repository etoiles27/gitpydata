import pandas as pd


data = {
'영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
'개봉 연도' : [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015],
'관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (단위 : 만 명)
'평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}

# Dataframe . index 1번 -8번 지정. 
# index 이름 지정 : 영화번호

ind = ['1번','2번','3번','4번','5번','6번','7번','8번']

#  index 넣기
df = pd.DataFrame(data, index=ind)
# index 이름지정 
df.index.name='영화번호'
# inplace에 넣기 
df.reset_index(inplace=True)
# 인덱스 삭제 
df.reset_index(drop=True,inplace=True)
# 영화인덱스 설정
df.set_index('영화',inplace=True)
print(df)
# 순차정렬
df.sort_index(ascending=True, inplace=True)
print(df)
# 역순정렬
df.sort_index(ascending=False, inplace=True)
print(df)

