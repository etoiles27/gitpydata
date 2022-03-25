# 학생성적 프로그램
# 입력, 출력
# ex0324_07.py -> main
# stuclass.py -> class
# stu_func.py  ->함수

import stuclass as st
from stu_func import *


stuSave = [] # 객체로 넣고 객체로 출력 

while True:
    
    user_choice = 0
    user_choice = mainpage(user_choice)
    if user_choice == 1:
        stu_input(stuSave)
    elif user_choice == 2:
        stu_modify(stuSave)    
    elif user_choice == 5:
        stu_all(stuSave)
    elif user_choice == 0:
        break
    elif user_choice == 9:
        pass


    
