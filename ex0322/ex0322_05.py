import os

# # 파일 쓰기
# with open('num.txt','a',encoding='utf-8') as file:
#     file.write('6\t김유신\t100\t100\t200\t100.0\t0\n')

# # 파일 읽어오기
# with open('num.txt','r',encoding='utf-8') as file:
#     print(file.read()) # 한번에 전부 읽기

# with open('num.txt','r',encoding='utf-8') as file:
#     print(file.readline(),end='') # 한번에 한줄 읽기 

    
    
# # 한줄씩 읽어서 전체 문장 출력
# with open('num.txt','r',encoding='utf-8') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line,end='') # 한번에 한줄 읽기 

with open('num.txt','r',encoding='utf-8') as file:
    lines=file.readlines()
    for line in lines:
        print(line,end='')
        
