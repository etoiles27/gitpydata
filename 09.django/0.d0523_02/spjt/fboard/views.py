from django.shortcuts import redirect, render
from fboard.models import Fboard
from member.models import Member
from django.db.models import F

def fList(request):
    qs = Fboard.objects.all().order_by('-f_group','f_indent')
    context = {'fList':qs}    
    return render(request,'fList.html',context)


def fView(request,f_no):
    qs = Fboard.objects.get(f_no=f_no)
    context = {'board':qs}    
    return render(request,'fView.html',context)

def fWrite(request):
    if request.method =='GET':
        return render(request,'fWrite.html')
    else:
        id = request.POST.get('id')
        member = Member.objects.get(id=id)
        title = request.POST.get('title')
        content = request.POST.get('content')
        file = request.POST.get('file',None)
        qs = Fboard(member=member,f_title=title,f_content=content,f_file=file)
        qs.save()
        qs.f_group=qs.f_no
        qs.save()
        return redirect('fboard:fList')

def fDelete(request,f_no):
    qs = Fboard.objects.get(f_no=f_no)
    qs.delete()
    return redirect('fboard:fList')


def fUpdate(request,f_no):
    if request.method =='GET':
        qs = Fboard.objects.get(f_no=f_no)
        context={'board':qs}
        return render(request,'fUpdate.html',context)
    else:
        
        qs = Fboard.objects.get(f_no=f_no)
        qs.f_title = request.POST.get('title')
        qs.f_content = request.POST.get('content')
        qs.f_file = request.POST.get('file')
        
        qs.save()
          
        return redirect('fboard:fList')
    
    
def fReply(request,f_no):
    if request.method =='GET':
        qs = Fboard.objects.get(f_no=f_no)
        context={'board':qs}
        return render(request,'fReply.html',context)
    else:
        
        qs = Fboard.objects.get(f_no=f_no)
        
        id = request.POST.get('id')
        member = Member.objects.get(id=id)
        title = request.POST.get('title')
        content = request.POST.get('content')
        file = request.POST.get('file',None)
        
        Fboard.objects.filter(f_group=qs.f_group,f_step__gt=qs.f_step).update(f_step=F('f_step')+1)
        f_group = int(qs.f_group)
        f_step = int(qs.f_step) + 1
        f_indent = int(qs.f_indent) + 1       
                    
        qs = Fboard(member=member,f_title=title,f_content=content,f_file=file,f_group=f_group,f_step=f_step,f_indent=f_indent)
        qs.save()
        
     
          
        return redirect('fboard:fList')
    
