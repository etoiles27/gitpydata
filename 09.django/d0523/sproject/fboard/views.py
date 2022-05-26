from django.shortcuts import redirect, render
from fboard.models import Fboard
from member.models import Member
from django.db.models import F 
from django.core.paginator import Paginator



# 게시판 리스트 함수 
def fList(request,nowpage):
    qs = Fboard.objects.all().order_by('-f_group','f_step')
    # page = int(request.GET.get('nowpage',1))
    paginator = Paginator(qs,10) 
    fList = paginator.get_page(nowpage)
    context = {'fList':fList,'nowpage':nowpage}
    return render(request,'fList.html',context)

def fWrite(request,nowpage):
    if request.method == 'GET':
        context={'nowpage':nowpage}
        return render(request,'fWrite.html',context)
    else:
        id = request.POST.get('id')
        member = Member.objects.get(id=id)
        title = request.POST.get('title')
        content = request.POST.get('content')
        # file = request.POST.get('file',None)
        file=request.FILES.get('file',None)
        
        
        qs = Fboard(member=member,f_title=title,f_content=content,f_file=file)
        qs.save()
        qs.f_group=qs.f_no
        qs.save()
        return redirect('fboard:fList',nowpage)

def fView(request,f_no,nowpage):
    qs = Fboard.objects.get(f_no=f_no)
    qs.f_hit += 1
    qs.save()
    context = {'fList':fList,'nowpage':nowpage}
    return render(request,'fView.html',context)


def fReply(request,f_no,nowpage):
    if request.method == 'GET':
        qs = Fboard.objects.get(f_no=f_no)
        context = {'board':fList,'nowpage':nowpage}
        return render(request,'fReply.html',context)
    else:
        id = request.POST.get('id')
        group = int(request.POST.get('group'))
        step = int(request.POST.get('step'))
        indent = int(request.POST.get('indent'))
        
        member = Member.objects.get(id=id)
        title = request.POST.get('title')
        content = request.POST.get('content')
        # file = request.POST.get('file',None)
        file=request.FILES.get('file',None)
        
        # reboard = Fboard.objects.filter(f_group=group,f_step__gt=step)
        # reboard.update(f_step=F('f_step')+1)
        Fboard.objects.filter(f_group=group,f_step__gt=step).update(f_step=F('f_step')+1)
        qs = Fboard(member=member,f_title=title,f_content=content,f_group=group,f_step=step+1,f_indent=indent+1,f_file=file)
        
        qs.save()
        return redirect('fboard:fList',nowpage)

def fDelete(request,nowpage,f_no):
    qs = Fboard.objects.get(f_no=f_no)
    qs.delete()
    return redirect('fboard:fList',nowpage)


def fUpdate(request,f_no,nowpage):
    if request.method == 'GET':
        qs = Fboard.objects.get(f_no=f_no)
        context = {'fList':fList,'nowpage':nowpage}
        return render(request,'fUpdate.html',context)
    else:        
        qs = Fboard.objects.get(f_no=f_no)

        qs.f_title = request.POST.get('title')
        qs.f_content = request.POST.get('content')
        file = request.POST.get('file',None) 

        if file:
            qs.f_file=file
        else:
            qs.f_file = request.FILES.get('file',None) 
        
        qs.save()     
        return redirect('fboard:fList',nowpage)