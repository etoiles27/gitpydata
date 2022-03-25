# 3의 배수는 제외하고
# 100이 넘을때의 총합과 숫자를 출력하세요 

sum = 0 
i = 0 
for i in range(1,101):
    
    if i%3 == 0:
       continue
    else:
        sum += i 
    if sum >100:
        break

print('{} 일때 총합은 {} 입니다.'.format(i,sum))
