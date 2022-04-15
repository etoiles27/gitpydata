data = [1,1,1,2,2,3,3,3]
j=0
mylist=[]
mylist.append(data[0])    
for i in range(len(data)):
    while mylist[j]!=data[i]:
        mylist.append(data[i])
        j=j+1

print(mylist)


