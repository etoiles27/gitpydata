from django.shortcuts import render
from students.models import Student

# Create your views here.
def register(request):
    
    
    # qs= Student(s_name="홍길동",s_major="컴퓨터공학과",s_age=20,s_grade=1,s_gender="남자")
    # qs.save()
    # qs= Student(s_name="이순신",s_major="체육교육학과",s_age=23,s_grade=2,s_gender="남자")
    # qs.save()
    # qs= Student(s_name="유관순",s_major="간호학과",s_age=21,s_grade=2,s_gender="여자")
    # qs.save()
    # qs= Student(s_name="강감찬",s_major="경영학과",s_age=24,s_grade=4,s_gender="남자")
    # qs.save()
    # qs= Student(s_name="김구",s_major="국어국문학과",s_age=22,s_grade=3,s_gender="남자")
    # qs.save()
    
    qs1 = Student.objects.all()
    print(qs1)
    
    qs2 = Student.objects.get(s_name='유관순')
    print(qs2)
    
    qs3 = Student.objects.get(s_name='강감찬')
    qs3.s_grade = 3
    qs3.save()
    
    # qs4 = Student.objects.get(s_name='강감찬')
    # qs4.delete()
    # print('삭제 되었습니다.')
    
    
    
    
    return render(request, 'register.html')