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
batter = pd.read_csv('C:/pydata/10.mlearn/m0713/batter_stats_2017.csv')

# Index(['선수명', '팀명', '경기', '타석', '타수', '안타', '홈런', '득점', '타점', '볼넷', '삼진', '도루', 
#    'BABIP', '타율', '출루율', '장타율', 'OPS', 'wOBA', 'WAR', '연봉(2018)', '연봉(2017)'],
# print(batter.columns)
# print(batter.describe())
# print(batter.info())
# print(batter[batter['BABIP'] == '-'] )

# batter['BABIP'] = pd.to_numeric(batter['BABIP'])



batter_df = batter.drop(columns=['연봉(2018)','선수명','팀명'])
batter_label = batter['연봉(2018)'].to_numpy()

ss = StandardScaler()
batter_scaled = ss.fit_transform(batter_df.to_numpy())

train_data, test_data, train_label, test_label = train_test_split(batter_scaled, batter_label, random_state=19)





lr = LinearRegression()
lr.fit(train_data,train_label)

print(lr.score(train_data,train_label))
print(lr.score(test_data,test_label))

cols = ['경기', '타석', '타수', '안타', '홈런', '득점', '타점', '볼넷', '삼진', '도루', 
    'BABIP', '타율', '출루율', '장타율', 'OPS', 'wOBA', 'WAR', '연봉(2017)']



corr = batter_df[cols].corr(method='pearson')
show_cols = ['game','PA','AB','hit','homerun','run','RBI','ball4','strike3','SB','BABIP','AVG','OBP',
             'SLG','OPS','wOBA','WAR','2017']

    

hm = sns.heatmap(corr.values,
                 cbar=True,
                 annot=True,
                 square=True,
                 fmt='.2f',
                 annot_kws={'size':15},
                 yticklabels=show_cols,
                 xticklabels=show_cols)
# plt.show()
print(corr)


vif = pd.DataFrame()
vif['VIF factor'] = [variance_inflation_factor(batter_df.values,i) for i in range(batter_df.shape[1])] 
vif['features'] = batter_df.columns
print(vif.round(1))





X = batter[['타수','안타','타율','wOBA','WAR','연봉(2017)']]
Y = batter['연봉(2018)'].to_numpy()


ss = StandardScaler()
X_scaled = ss.fit_transform(X.to_numpy())


train_data, test_data, train_label, test_label = train_test_split(X_scaled, Y,random_state=19)

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

