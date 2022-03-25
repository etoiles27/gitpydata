import os

# print(os.name)
# print(os.getcwd()) # 현재위치
# print(os.listdir()) # 현재폴더안에 있는것

# with open('num.txt','w',encoding='utf-8') as file: # w 는 덮어쓰기 #a 는 추가 
#     file.write("안녕\n")
#     file.write("반가워\n")

# with open('num.txt','a',encoding='utf-8') as file:
#     file.write('다시 글을 입력합니다. \n')

# file = open('num.txt','a',encoding='utf-8')
# file.write('글을 다른형태로 쓰기도합니다.')
# file.close() # open을 받는 파일에서는 꼭 close를 해야한다. 

with open('num.txt','w',encoding='utf-8') as file:
    file.write('1\t홍길동\t100\t100\t200\t100.0\t0\n')
    file.write('2\t유관순\t100\t100\t200\t100.0\t0\n')
    file.write('3\t이순신\t100\t100\t200\t100.0\t0\n')
    file.write('4\t강감찬\t100\t100\t200\t100.0\t0\n')
    file.write('5\t김구\t100\t100\t200\t100.0\t0\n')