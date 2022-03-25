# tlist = [4,6,1,8,9,11,2]
# tlist2 = sorted(tlist) # 기존 리스트는 변경되지 않고 새로운 정렬된 리스트생성 
# # tlist.sort()
# print(tlist)
# print(tlist2)

import operator
import re

tdic, tlist = {},[]
tdic = {'love':'사랑','chair':'의자','game':'게임','car':'자동차'}
tlist= sorted(tdic.items(),key=operator.itemgetter(0))
print(tlist)

tlist2 = list(tdic.items())
tlist2.sort(reverse=True)
print(tlist2)