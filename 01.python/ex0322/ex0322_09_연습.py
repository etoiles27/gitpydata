import os


#print(os.listdir())
# 파일이 있는지 확인. 
if '2.txt' in os.listdir():
    print('잇음')
    with open('2.txt','a',encoding='utf-8') as file:
        file.write('파일을 추가해서 저장\n')
        
else:
    print('없음')
    with open('2.txt','w',encoding='utf-8') as file:
        file.write('새로운 파일 저장\n')

# 문제: 파일 이름을 입력받아.
# 파일이 있으면, 파일 이름을 1_1.txt로 변경해서 저장하시오 같은 이름이 있으면 "_.txt"
# 조건, 동일한 파일 이름이 있으면. 1_1.txt로 변경해서 저장하세요 


# str1 = '1.txt'
# n= str1.index('.')
# str2 =str1[:n]+'_1'+str1[n:]
# print(str2)

str1 = input('파일명을 입력하세요 ')


lines1 = []
if str1 in os.listdir():
    # 같은 이름이 있을 경우 _.txt 파일 생성
    n= str1.find('.')
    str2 =str1[:n]+'_1'+str1[n:]
    with open(str2,'w',encoding='utf-8') as file: 
        count = 0
        while True:
            str3= input("{}줄 내용을 입력하세요 (종료0) >>  ".format(count+1))
            if str3 == '0':
                break
            file.write(str3)
            file.write('\n')
            count +=1
    
    # #기존의 파일을 읽어서 리스트에 저장
    # with open(str1,'r',encoding='utf-8') as file:
    #     lines=file.readlines()
    #     for line in lines:
    #         lines1.append(line)
    # # 기존 파일 내용이 적힌 리스트를 새로운이름의 파일에 저장 
    # with open(str2,'w',encoding='utf-8') as file: 
    #     for line in lines1:
    #         file.writelines(line)
else:
    with open(str1,'w',encoding='utf-8') as file: 
        count = 0
        while True:
            str3= input("{}줄 내용을 입력하세요 (종료0) >>  ".format(count+1))
            if str3 == '0':
                break
            file.write(str3)
            file.write('\n')
            count +=1
        
        
    
        
        
# print(lines)


