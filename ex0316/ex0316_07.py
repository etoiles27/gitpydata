words = {
    '자동차':'car', 
    '의자':'chair',
    '사랑':'love',
    '국수':'noodle',
    '돼지':'pig',
    '호랑이':'tiger',
    '직업':'job',
    '사과':'apple',
    '사자':'lion'
}
words2 = {
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


wordlist=[] # 출력때 쓸 리스트 [입력한 값, 정답여부] 

for word in words:
    inwds= input('{}의 영어단어를 입력하세요 (0: 종료) >>  '.format(word))
    
    if inwds.isdigit():
        if int(inwds)==0:
            print('프로그램을 종료합니다')
            break
    if words[word] == inwds:
        # print('정답입니다!! {} : {}'.format(word,words[word]))
        wlist = [inwds,'o']
        wordlist.append(wlist)
    else:
        # print('오답입니다!! 정답은 {} : {} 입니다'.format(word,words[word]))
        wlist = [inwds,'x']
        wordlist.append(wlist)

ocnt,xcnt=0,0
print('-'*50)
print(' [ 정답 확인 ] ')
print('-'*50)
for i, wlist in enumerate(wordlist):
    if 'o' in wlist:
        ocnt += 1
        print('{}. 정답 -> {} : {} 입니다 '.format(i+1,list(words.keys())[i],list(words.values())[i]))
    else:
        xcnt += 1
        print('{}. 오답 -> 입력한 값: {} 정답은 {} : {} 입니다'.format(i+1,wlist[0],list(words.keys())[i],list(words.values())[i]))

print("정답 : {} 개, 오답 : {} 게 \n총점: {} 점".format(ocnt,xcnt,ocnt*10))