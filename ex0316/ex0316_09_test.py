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

# 1. total list = [] 키 : word1, word2 각각 랜덤하게 5개를 담아보세요 -> total_list : 10개  출력하세욤 
# 2. tdic = {key:value}를 출력하세요
# 3. word1, word2의 개수를 입력받아 리스트에 담아보세요 

total_list = []
tdic = {}
word1_list = list(word1.keys())
word2_list = list(word2.keys())

u_input = 0
cnt1 = 0
cnt2 = 0
while True:
    u_input = int(input('첫번째 단어장에서 가저올 단어의 개수를 입력하세요 0-10 (종료:100) >> '))
    if u_input == 100:
        break
    
    while cnt1 < u_input:
        rno1 = randint(0,len(word1_list)-1)
        if not word1_list[rno1] in total_list:
            total_list.append(word1_list[rno1])
            cnt1 += 1
    # print('첫번째 단어장에서 선택된 단어 : ',total_list)
    while cnt2 < (10-u_input):
        rno2 = randint(0,len(word2_list)-1)
        if not word2_list[rno2] in total_list:
            total_list.append(word2_list[rno2])
            cnt2 += 1
            
    print('첫번째 단어장 {}개의 단어, 두번재 단어장 {}개의 단어로 구성된 단어 \n{}'.format(u_input,10-u_input,total_list))
    


    for i in range(len(total_list)):
        if total_list[i] in word1:
            tdic[total_list[i]] = word1[total_list[i]]
        elif total_list[i] in word2:
            tdic[total_list[i]] = word2[total_list[i]]


    print(tdic)
    total_list=[]
    cnt1 = 0
    cnt2 = 0