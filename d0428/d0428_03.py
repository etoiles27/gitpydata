# dataframe 
# 2차원 배열
import pandas as pd

data = {
    '학번': [1,2,3,4],
    '이름': ['홍길동','홍길자','홍길순','이순신'],
    '국어': [100,90,80,70],
    '영어': [100,90,80,70]
}


print(data)

temp = pd.DataFrame(data)

print(temp)