from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import SGDClassifier, LogisticRegression,LinearRegression
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from scipy.special import expit,softmax
from sklearn.tree import DecisionTreeClassifier, plot_tree
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor

# 한글설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'Apple Gothic' # apple사용시
matplotlib.rcParams['font.size'] = 15 # 상단제목 글자 15크기 변환
matplotlib.rcParams['axes.unicode_minus']=False # 눈금 -표시 처리

# 투수 - 2018 연봉예측 알고리즘
df = pd.read_csv('C:/pydata/10.mlearn/m0707/picher_stats_2017.csv')

# one_encoding=pd.get_dummies(df['팀명'])
# df = df.join(one_encoding)

# pi_data = df.drop(columns=['연봉(2018)','선수명','팀명']).to_numpy()
# pi_label = df['연봉(2018)'].to_numpy()

# 데이터 전처리 - 정규화, 표준화 작업이 필요
# train_data, test_data, train_label, test_label = train_test_split(pi_data, pi_label, random_state=42)



def standatd_scaling(df, scale_columns): # 전체데이터, 컬럼리스트
    for col in scale_columns:
        seris_mean = df[col].mean()
        seris_std = df[col].std()
        df[col] = df[col].apply(lambda x:(x-seris_mean)/seris_std)
    return df


scale_columns = ['승', '패', '세', '홀드', '블론', '경기', '선발', '이닝', '삼진/9',
       '볼넷/9', '홈런/9', 'BABIP', 'LOB%', 'ERA', 'RA9-WAR', 'FIP', 'kFIP', 'WAR',
       '연봉(2017)']

# 정규화
picher_df= standatd_scaling(df, scale_columns)
picher_df = picher_df.rename(columns={'연봉(2018)':'y'})
# 원핫인코딩 - 컬럼 글자 제거를 위한. 
one_encoding = pd.get_dummies(picher_df['팀명'])
picher_df=picher_df.join(one_encoding)

# 
data = picher_df[picher_df.columns.difference(['y','선수명','팀명'])]
pi_data = picher_df.drop(columns=['y','선수명','팀명']).to_numpy()
pi_label = picher_df['y'].to_numpy()

train_data, test_data, train_label, test_label = train_test_split(pi_data, pi_label,random_state=19)

lr = LinearRegression()
lr.fit(train_data, train_label)
score_tr = lr.score(train_data, train_label)
score_te = lr.score(test_data, test_label)
print(score_tr)
print(score_te)


scale_columns1 = ['승', '패', '세', '홀드', '블론', '경기', '선발', '이닝', '삼진/9',
       '볼넷/9', '홈런/9', 'BABIP', 'LOB%', 'ERA', 'RA9-WAR', 'FIP', 'kFIP', 'WAR',
       'y', '연봉(2017)']
# 컬럼 영향력 파악분석
corr = picher_df[scale_columns1].corr(method='pearson')
show_cols = ['win','lose','save','hold','blon','game','start','inning','strike3','ball4','homerun','babip','lob','era','ra9-war','fip','kfip','war','2017']
hm = sns.heatmap(corr.values, cbar=True, annot=True, square=True, fmt='.2f',annot_kws={'size':15},yticklabels=show_cols, xticklabels=show_cols)
# plt.show()
# print(corr)

vif = pd.DataFrame()
vif['VIF factor'] = [variance_inflation_factor(data.values,i) for i in range(data.shape[1])] 
vif['features'] = data.columns
print(vif.round(1))



X = picher_df[['kFIP','WAR','볼넷/9','삼진/9','연봉(2017)']]
Y = picher_df['y']
train_data, test_data, train_label, test_label = train_test_split(X, Y,random_state=19)

lr = LinearRegression()
lr.fit(train_data, train_label)
score_tr = lr.score(train_data, train_label)
score_te = lr.score(test_data, test_label)
print(score_tr)
print(score_te)


vif = pd.DataFrame()
vif['VIF factor'] = [variance_inflation_factor(X.values,i) for i in range(X.shape[1])] 
vif['features'] = X.columns
print(vif.round(1))



predict_2018_salary = lr.predict(test_data)
picher2 = pd.read_csv('C:/pydata/10.mlearn/m0707/picher_stats_2017.csv')
picher2['예측연봉(2018)'] = pd.Series(predict_2018_salary)

result_df = picher_df.sort_values(by=['y'], ascending=False)






print(picher2[['선수명','연봉(2017)','연봉(2018)' ,'예측연봉(2018)']])























# ss = StandardScaler()
# train_scaled = ss.fit_transform(train_data)
# test_scaled = ss.fit_transform(test_data)






# # 예측은 3개중에 하나 알고리즘을 선택하면된다 
# lr = LinearRegression()
# knn = KNeighborsRegressor()
# rs = RandomForestRegressor()

# 훈련 

# 정확도 


# print(df.describe())
# print(df.info())

# plt.scatter(df['선수명'],df['연봉(2018)'])
# plt.show()
# plt.hist(df['연봉(2018)'], bins=100)
# plt.show()
# df.boxplot(column=['연봉(2018)'])
# plt.show()

# def plot_hist(df):
#     plt.rcParams['figure.figsize']=[20,16]
#     fig = plt.figure(1)
#     for i in range(len(df.columns)): # 20번 
#         ax = fig.add_subplot(5,5,i+1)
#         plt.hist(df[df.columns[i]],bins=50)
#         ax.set_title(df.columns[i])
#     plt.show()
    
# picherdf = df.drop(columns=['선수명','팀명'])
# plot_hist(picherdf)


