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

# 타입은 리스트, 튜플형 
wlist = list(word1.items()) # key, value 가 살아 있다. 

count = 0
listtemp=[]
while count < 5 :
    rno = randint(0,9)
    if not wlist[rno] in listtemp:
        listtemp.append(wlist[rno])
        count += 1

print(listtemp)