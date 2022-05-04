# # tdic = {'pig':'돼지','tiger':'호랑이','lion':'사자','dog':'개'}

# # print(type(tdic))
# # dtuple = list(tdic.items())
# # dtuple.sort()
# # print(type(dtuple))
# # tdic = dict(dtuple)
# # print(type(tdic))
# # print(dtuple)

# numdic1 = {1,2,33,3,3,5,1,9,2,3}
# numdic2 = {2,3,4,5,2,3,9,10,11,13}

# # numdic3 = numdic1 - numdic2 
# # print(numdic3 )


# print(numdic1)
# print(numdic2)
# print(numdic1&numdic2) #교집합
# print(numdic1|numdic2) #합집합
# print(numdic1-numdic2) #차집합
# # numdic11 = set(numdic1)
# # print(numdic11)
# adic = {1:'aaa',2:'bbb',3:'ccc',1:'ddd'}
# print(adic)

# #numdic2 = {4,5,2,9,10,15,30,20,7,8}


# # # 파이썬에선 set 이라는 개념이 있다 
# # # set을 하게되면 중복을 지워준다. 
# # numdic1 = set(numdic1)

# nlist1 = [1,2,5,4,8]
# nlist2 = [3,4,5,8,2]
# print(nlist1+nlist2)

# print('-'*30)

# dic1 = {'no':1,'name':'mini','add':'apt','phone':123}
# dic2 = {'food':'cake','drink':'coffee','name':'mini'}

# dic3 = dic1 | dic2

# print(dic3)


# a ={1,2,4}

# myset={1,2,3,4,5,5}
# print(myset)

# mylist=[9,12,4,4,5,5,1,2,6,7,8]
# myset = set(mylist) # 자동 중복지워주고, 자동정렬된다 . 
# mmylist = list(myset) # 리스트로 변경
# print(myset)
# print(mmylist)

# set에 추가 삭제 
myset = {1,2,3}
myset.add(4)
myset.remove(2)
myset.clear()
print(myset)