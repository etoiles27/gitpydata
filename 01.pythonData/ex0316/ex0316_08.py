from random import *

word1 = {
    '자동차':'car', 
    '의자':'chair',
    '사랑':'love',
    '국수':'noodle',
    '돼지':'pig',
    '호랑이':'tiger',
    '직업':'job',
    '사과':'apple',
    '사자':'lion',
    '여우':'fox'
}
word2 = {
    '연필':'pencil', 
    '자':'ruler',
    '책':'book',
    '양말':'sock',
    '모자':'hat',
    '개':'dog',
    '잠':'sleep',
    '먹다':'eat',
    '읽다':'read',
    '피아노':'piano'
}

# 랜덤으로 5개 뽑는다. 
rno = randint(0,len(word1))

# print(list(word1.keys())[rno])
# word에서 랜덤하게 5개의 키를 뽑아 저장한다. 
randtemp=[]
# word1에서 키를 뽑아 저장
level1 = list(word1.keys())
cnt = 0
while cnt<5:
    rno = randint(0,len(word1)-1)
    if not level1[rno] in randtemp:
        randtemp.append(level1[rno]) 
        cnt += 1
    else:
        continue
    
print(randtemp)

dic ={}
for i in range(5):
    dic[randtemp[i]] = word1[randtemp[i]]

print(dic)