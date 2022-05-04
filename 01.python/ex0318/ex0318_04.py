

# 1001 학번이 있다. 
# 를 붙여서 학번을 출력 
# s가 붙어 있으면 a로 변경해서 출력
# ex) 1001 -> s1001 , s1002 ->al002
# startwith 함수 사용 

# input_num = input("학번을 입력하세요 >> ")

# # if input_num.startswith('a'):
# #     st_num = 't'+input_num[1:len(input_num)]    
# # else:
# #     if input_num[0].isdigit():
# #         st_num = 's'+input_num
# #     else:
# #         st_num = 't'+input_num[1:]

# if input_num[0].isdigit():
#     st_num = 's'+input_num    
# else:
#     st_num = 't'+input_num[1:]


# print(st_num)



# 신규 주민번호를 만들었는데, 구주민번호를 사용하는사람들이 있다.
# 구주민번호를 사용하는 사람들의 주민번호를 신규주민번호로 만들어주는 프로그램
# 00년생 (22살) 
# 23 이상 ~ 100세 이하의 사람만 있는 사이트가 있다. 
# 8번째 자리가 1,2 로 시작하면 19로 붙여준다 
# 예: 990101-1105555  -> 19990101-1105555
# 예: 990101-2105555  -> 19990101-2105555 
# 예: 010101-3105555  -> 20010101-3105555
# 예: 010101-4105555  -> 20010101-4105555

# u_input = input('주민번호를 입력해주세요 >> ')

# if u_input[7] == '1' or '2'or '5'or '6':
#      u_input = '19'+u_input
# elif u_input[7] == '3' or '4' or '7' or '8':
#      u_input = '20'+u_input
# else:
#     print("번호를 잘못입력했습니다. 다시입력해주세요")
# print(u_input)


