# # 입력된 문자의 첫글자가 대문자인지 ?

# input1 = input("영어를 입력하세요 >> ")

# if input1[0].isupper():
#     print("대문자로 시작합니다.")
# else:
#     print("소문자로 시작합니다.")


# 입력된 문자의 시작이 >> 로 시작하는지 확인해서
# >>로 시작하지 않으면 >>를 입력하세요

input1 = input("문자를 입력하세요 >> ")
if not input1.startswith('>>'):
    input1='>>'+input1
print(input1)