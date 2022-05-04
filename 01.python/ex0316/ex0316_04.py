
student = {
    'id' : 'aaa', 'pass':'1111', 'name':'홍길동','tel':'010-0000-0000',
    'address':'서울', 'gender':'male', 'hobby':'game'
}

# 1. 키값 검색 
# 2. value값 검색
# 3. 딕셔너리 전체출력
# 원하는 번호입력
# 프로그램 구성

input_num = 100

while True:
    print('1. 키값 검색')
    print('2. value값 검색')
    print('3. 딕셔너리 전체출력')
    input_num = input('원하는 값을 입력하세요 (종료: 4) >> ')
    print('-'*40)
    if not input_num.isdigit():
        print('숫자만 입력이 가능합니다.')
        print('-'*40)
        continue
    input_num = int(input_num)
    
    if input_num == 1:
        while True:
            key1 = input('검색하고 싶은 키값을 입력해주세요 (0번 상위메뉴이동) >> ')
            if key1.isdigit():
                if int(key1)==0:
                    print('\n상위 메뉴로 이동합니다. ')
                    break
            
            if key1 in student:
                print('\n키가 있습니다. ')
                print()
            else:
                print('\n키가 없습니다. ')
                print()
            # print(list(student.keys()))
    elif input_num == 2:
        while True:
            val1 = input('검색하고 싶은 value 값을 입력해주세요 (0번 상위메뉴이동) >> ')
            if val1.isdigit():
                if int(val1)==0:
                    print('\n상위 메뉴로 이동합니다. ')
                    break
            if val1 in student.values():
                print('\nvalue가 있습니다. >> ')
                for k in student:
                    if student[k] == val1:
                        print('key 가 {} 일 때,  {} 값이 있습니다.'.format(k,val1))
            else:
                print('\nvalue가 없습니다. ')
            #print(list(student.values()))
        
        
        
    elif input_num == 3:
        for keys in student:
            print('{:10s} :  {} '.format(keys,student[keys]))
    elif input_num == 4:
        break
    print('-'*40)
    