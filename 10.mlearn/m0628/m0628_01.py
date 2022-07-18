

from sklearn import svm, metrics
from sklearn.neighbors import KNeighborsClassifier

data = [[0,0],[1,0],[0,1],[1,1]]
label = [0,1,1,0]
example = [[0,0],[1,0]]
example_label = [0,1]

clf= svm.SVC()
# clf = KNeighborsClassifier()
clf.fit(data,label)

results = clf.predict(example)
print(results)

score = metrics.accuracy_score(example_label,results)
print("정답률",score)


#	T1909519980