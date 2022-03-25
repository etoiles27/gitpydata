myList = [30,10,20]
print('현재 리스트 : {}'.format(myList))

myList.append(40)
print('append(40) 후의 리스트 : {}'.format(myList))

print('pop()으로 추출한 값 : {}'.format(myList.pop()))
print('pop()후의 리스트 : {}'.format(myList))

myList.sort()
print('sort() 후의 리스트 : {}'.format(myList))

myList.reverse()
print('reverse() 후의 리스트 : {}'.format(myList))

print("20 값의 위치 : {}".format(myList.index(20)))

myList.insert(2,222)
print('insert(2,222) 후의 리스트 : {}'.format(myList))

myList.remove(222)
print('remove(222) 후의 리스트 : {}'.format(myList))

myList.extend([77,88,77])
print('extend[77,88,77] 후의 리스트 : {}'.format(myList))

print('77 값의 개수 : {}'.format(myList.count(77)))

