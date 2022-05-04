



aa = [1,2,3,4,5,6,7,8,9]

print(aa)

# 삭제 방법 

aa[1:4]=[] # 슬라이싱 삭제
print(aa)

aa=[] # 비우기 , 리스트가 살아 있다
print(aa)
print(type(aa))



aa=None # 타입이: none  변수는 살아 잇다. 
print(aa)
print(type(aa))

aa = [1,2,3,4,5,6,7,8,9]
del(aa) # 완전히 삭제되어 type도 없다 변수 자체도 없다 -> error


aa = [1,2,333,4,6,555,6,77,8,9]

# # list에 데이터를 검색해서 , 그 검색된 데이터를 삭제 (첫번째꺼만.. 다 지우려면 for 문을 돌려 삭제해야한다. )
# # 데이터 값으로 삭제 
# aa.remove(333)

# for i in range(len(aa)):
#     if 6 in aa:
#         aa.remove(6)

# aa.clear() # 변수 전체삭제 타입은 그대로 리스트 살아있다. 
# aa.pop() # 맨 뒤 변수 삭제 

# aa.sort() # 순차정렬
# aa.reverse() # 입력한 항목을 역순으로 출력

# aa.sort(reverse=True) #역순정렬

# aa.insert(2,100) # 특정한 위치에 넣기 . 2번장소에 100 이란 값을 넣기
# aa.append(55) # 젤 뒤에 변수 넣기

# idx = aa.index(77) # 찾는 데이터의 위치를 알 수 있다.  (있는 위치를 알 수 있다. )
# print(idx)

# n = aa.count(6) # 찾고자 하는데이터의 갯수를 알려준다. (6이 몇개 있는지를 세준다.)
# print(n)

# aa.extend([1,2,3]) # list에 추가한다. list를 넣어야한다. append는 한개, extend는 여러개 . 리스트 + 와 같다

dd = aa # 얕은 복사 -> 같은 주소를 바라본다.
bb = aa.copy() # 깊은 복사. 새로운 저장장소를 만들어 할당해준다
bb.append(5)
cc = sorted(aa)  # 새롭게 저장장소를 만들어 값을 넣는다. 
aa.append(100)



print('aa : ',aa)
print('bb : ',bb)
print('cc : ',cc)
print('dd : ',dd)

