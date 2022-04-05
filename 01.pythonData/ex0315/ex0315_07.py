numbers = [273,103,5,32,65,9,72,800,90]

chk = ['짝수','홀수']
for n in numbers:
    if n>=100:
        print('100 이상의 수 : {}'.format(n))
        
# for n in numbers:
#     if n%2 == 0:
#         print('{:5d} : 짝수'.format(n))
#     else:
#         print('{:5d} : 홀수'.format(n))
    
for n in numbers:
    print('{:5d} : {:3s}'.format(n,chk[n%2]))