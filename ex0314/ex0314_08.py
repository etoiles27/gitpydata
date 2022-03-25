# a = input("문자를 입력하세요 >> ")
# if a =='$':
#     print("$ 문자입니다")
# else:
#     print("$ 문자가 아닙니다")




total, i =  0, 0
for i in range(1,100):
    total += i
    if total > 100 :
        break
print('총 합은 {} 입니다'.format(total))
print('100을 넘었을때 수는 {} 입니다'. format(i))