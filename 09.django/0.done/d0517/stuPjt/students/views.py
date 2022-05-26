from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from students.models import Student

# Create your views here.

# 학생등록페이지
def stuWrite(request):
    if request.method == 'GET':
        
        return render(request,'stuWrite.html')
        
    else:
        # 받은 데이터 읽기 (from form)
        name = request.POST.get('name')
        major = request.POST.get('major')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        gender = request.POST.get('gender')
        
        print('form name : ', name)

        Student.objects.create(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender)
        
        
        return HttpResponseRedirect(reverse('index'))
    
    
def stuList(request):
    # qs = Student.objects.all()
    # count = qs.count()
    # # dict type 로 html에 전달 
    # context = {'stuList':qs,'stuCount':count}

    qs = Student.objects.order_by('s_name')
    count = qs.count()
    context = {'stuList':qs,'stuCount':count}

    
    return render(request,'stuList.html',context)

def stuView(request, name):
    qs = Student.objects.get(s_name=name)
    context = {'stu':qs}
    return render(request,'stuView.html',context)

# def stuView(request):
#     name= request.GET.get('name')
#     qs = Student.objects.get(s_name=name)
#     context = {'stu':qs}
#     return render(request,'stuView.html',context)



# def stuView(request):

#     return render(request,'stuView.html')







# # 학생 db 등록 - from data 전달 받음
# def stuWriteOK(request):
#     # 받은 데이터 읽기 (from form)
#     name = request.POST.get('name')
#     major = request.POST.get('major')
#     age = request.POST.get('age')
#     grade = request.POST.get('grade')
#     gender = request.POST.get('gender')
    
#     print('form name : ', name)
    
#     # qs = Student(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender)
#     # qs.save()
#     # Student.objects.all()
#     # Student.objects.get(s_name='홍길동')
#     Student.objects.create(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender)
    
    
#     return HttpResponseRedirect(reverse('index'))
    
#     
    




# DB 명령어
# #  db 접근해서 정보를 가저올 예정 
    
    # # # create 
    # # qs1= Student(s_name="홍길순",s_major="영문학과",s_age=24,s_grade=4,s_gender="여자")
    # # qs1.save()
     
    # # read    
    # qs = Student.objects.all()
    # print(qs)
    
    # # read one data
    # qs2 = Student.objects.get(s_name='홍길동')
    # print(qs2)
    
    # # filter 
    # qs3 = Student.objects.filter(s_name__contains='홍')
    # print(qs3)
    
    # # update 
    # qs4 = Student.objects.get(s_name='홍길동')
    # qs4.s_major = '아동학과'
    # qs4.save()
    # print('변경되었습니다.')
    
    # delete 
    # qs5= Student(s_name="유관순",s_major="음악학과",s_age=25,s_grade=4,s_gender="여자")
    # qs5.save()
    # qs6= Student.objects.get(s_name="홍길자")
    # qs6.delete()
    # print('삭제되었습니다.')
    