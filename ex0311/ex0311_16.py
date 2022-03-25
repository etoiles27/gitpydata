

# 1-25 까지 list를 만들고 , 2차원 배열로 만들어보세요
# [[1,2,3,4,5],[6,7,8,9,10],.....]

# 1- 25 까지 배열을 만들기
num_lists = [i for i in range(1,26)]
print(num_lists)
# 2차원 배열 
arrs2 = [[],[],[],[],[]]
for  i, num_list in enumerate(num_lists):
    arrs2[i//5].append(num_list)   
print(arrs2)

    



# list1 = []
# list2 = []
# for  i, num_list in enumerate(num_lists):
#     if i < 5:
#         list1.append(num_list)
#     else:
#         list2.append(num_list)
        
# totallist = [list1,list2]

# print(totallist)



# for num in num_lists:
#     print('{:2d}'.format(num),end=' ')
#     if num%5 == 0:
#         print()