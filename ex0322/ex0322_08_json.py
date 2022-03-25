import json
 
data =[{'number': 1, 'name': '홍길동', 'kor': 100, 'eng': 100, 'total': 200, 'avg': 100.0, 'rank': 0},\
    {'number': 2, 'name': '바다', 'kor': 100, 'eng': 100, 'total': 200, 'avg': 100.0, 'rank': 0}] 


# # 만약 txt 파일로 저장한다면.. 
# with open('2.txt','w',encoding='utf-8') as file:
#     file.write('{}'.format(data[0]))


# with open('2.txt','r',encoding='utf-8') as file:
#     line = file.readline()
#     # print(type(line))
#     # print(type(dict(line))) # -> 불가능
#     print(line)

# # json 형태로 저장한다면.. 
# # 저장
# json.dump(data,open('1.json','w'))

# # 읽어오기
# data2 = json.load(open('1.json'))
# print(data2[1])





data3 = [{'number': 1, 'name': '홍길동', 'kor': 100, 'eng': 100, 'total': 200, 'avg': 100.0, 'rank': 0}, {'number': 2, 'name': '바다', 'kor': 100, 
'eng': 100, 'total': 200, 'avg': 100.0, 'rank': 0}, {'number': 3, 'name': '나비', 'kor': 100, 'eng': 100, 'total': 200, 'avg': 100.0, 'rank': 0}, {'number': 4, 'name': '우주', 'kor': 100, 'eng': 100, 'total': 200, 'avg': 100.0, 'rank': 0}]


json.dump(data3,open('3.json','w',encoding='utf-8'))
data4 = json.load(open('3.json',encoding='utf-8'))

for dat in data4:
    for key in dat.keys():
        print(key,end='\t')
    break
print()


for dat in data4:
    for v in dat.values():
        print(v,end='\t')
    print()
    