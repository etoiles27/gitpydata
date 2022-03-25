# 4개의 값을 입력받아 
# 합을구하고, 입력한 값을 출력하세요 

# inList = []
# sum = 0
# for i in range(4):
#     num = int(input('4개의 숫자를 입력하세요 >>'))
#     inList.append(num)
#     sum += num


# print('{} 의 총합 = {}'.format(inList, sum))

numbers = []
for i in range(4):
    numbers.append(int(input('enter the num : ')))

total = 0

for num in numbers:
    total += num

print('{} 의 총합 = {}'.format(numbers, total))
