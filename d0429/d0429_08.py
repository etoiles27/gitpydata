import pandas as pd




df = pd.read_excel('score.xlsx',index_col='지원번호')

# 조건식. and & or |

filt = df['이름'].str.startswith('김')
print(df[filt])