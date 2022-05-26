from django.http import HttpResponse
from django.shortcuts import redirect, render
from freeboard.models import Freeboard
from member.models import Member

# Create your views here.
def fList(request):
    qs = Freeboard.objects.all()
    context = {'fList':qs}
    return render(request,'fList.html',context)
    
def fView(request,f_no):
    qs = Freeboard.objects.get(f_no=f_no)
    
    context = {"fboard": qs}
    return render(request,'fView.html',context)

def fWrite(request):
    if request.method == 'GET':
        return render(request,'fWrite.html')
    else:
        id = request.POST.get('id')
        f_title = request.POST.get('title')
        f_content = request.POST.get('content')
        qs = Freeboard(id=id, f_title=f_title, f_content=f_content)
        qs.save()
        qs.f_group = qs.f_no
        qs.save()     
        return redirect('freeboard:fList')
    
    
def fDelete(request,f_no):
    qs = Freeboard.objects.get(f_no=f_no)
    qs.delete()
    
    return redirect('/freeboard/fList')


def fUpdate(request,f_no):
    
    if request.method == "GET": 
        qs = Freeboard.objects.get(f_no=f_no)
        context={"fboard":qs}
        return render(request,'fUpdate.html',context)
    else:
        qs = Freeboard.objects.get(f_no=f_no)
        qs.f_title = request.POST.get('title')
        qs.f_content = request.POST.get('content')
        qs.save()       
        return redirect('/freeboard/fList')