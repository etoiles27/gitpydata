from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from students.models import Student
# Create your views here.
def stuWrite(request):
    return render(request, 'stuWrite.html')

def stuWriteOk(request):
    name = request.POST.get('name')
    major = request.POST.get('major')
    age = request.POST.get('age')
    grade = request.POST.get('grade')
    gender = request.POST.get('gender')
    hobby =request.POST.getlist('hobby')   
    hobby = ','.join(hobby)
    Student.objects.create(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender,s_hobby=hobby)
    
    print('Student register done')      
    return HttpResponseRedirect(reverse('students:stuList'))  
    

def stuList(request):
    qs = Student.objects.all()
    count = qs.count()
    context = {'stuList':qs,'stuCount':count}
    return render(request, 'stuList.html',context)

def stuView(request,s_no):
    qs = Student.objects.get(s_no=s_no)
    data = {'stu':qs}
    return render(request, 'stuView.html',data)


def stuUpdate(request, s_no):
    qs = Student.objects.get(s_no=s_no)
    optlist=[1,2,3,4]
    data = {'stu':qs,'opt':optlist}
    return render(request, 'stuUpdate.html',data)


def stuUpdateOk(request):
    s_no = request.POST.get('s_no')
    major = request.POST.get('major')
    age = request.POST.get('age')
    grade = request.POST.get('grade')
    gender = request.POST.get('gender')
    hobby =request.POST.getlist('hobby')   
    hobby = ','.join(hobby)
    
    qs = Student.objects.get(s_no=s_no)
    qs.s_major=major
    qs.s_age =age
    qs.s_grade=grade
    qs.s_gender=gender
    qs.s_hobby = hobby
    
    qs.save()
    print('Student information update done')
    
    return  HttpResponseRedirect(reverse('students:stuList'))  


def stuDelete(request, s_no):
    qs = Student.objects.get(s_no=s_no)
    qs.delete()
    
    return  HttpResponseRedirect(reverse('students:stuList'))  
    