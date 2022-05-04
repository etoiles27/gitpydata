
import os

def strInput(str1,content):
    str1=input('파일 이름을 입력하세요(확장자명은 자동)')    
    str1 = str1+'.txt'
    print('저장할 내용을 입력하세요')
    count = 1
    while True:
        temp = input('{}줄 : '.format(count))
        if temp == '0' :
            break
        content.append(temp+'\n')
        count += 1
    return str1

def strfileSave(str1,content):
    if str1 in os.listdir():
        str1 = str1[:str1.find('.')]+'_1'+str1[str1.find('.'):]
        with open(str1,'w',encoding='utf-8') as file: 
            for i in range(len(content)):
                file.write(content[i])
    else:
        with open(str1,'w',encoding='utf-8') as file: 
            for i in range(len(content)):
                file.write(content[i])
                