foods ={
    '떡볶이':'오뎅', '짜장면':'단무지','라면':'김치','피자':'피클',
    '맥주':'땅콩','치킨':'치킨무','삼겹살':'상추'
}

print(foods)

print(foods.keys())

input1=100
while True:

    input1 = input('원하는 음식을 입력하세요 >> (종료: 0)')

    if input1.isdigit():
        if int(input1) == 0:
            break
    if input1 in foods.keys():
        print('{}의 짝꿍은 {} 입니다'.format(input1,foods[input1]))
    else:
        print('다시입력하세요')
        
    
    