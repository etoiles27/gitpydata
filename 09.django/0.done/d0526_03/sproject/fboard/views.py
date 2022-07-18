from unicodedata import category
from django.shortcuts import redirect, render
from fboard.models import Fboard
from member.models import Member
from django.db.models import F,Q 
from django.core.paginator import Paginator



# 게시판 리스트 함수 
def fList(request,nowpage,category,searchword):
    if request.method =="POST":
        category = request.POST.get('category')
        searchword = request.POST.get('searchword')
    
        

    
    # if category=='first':
 
    # if request.method =="GET":
        # qs = Fboard.objects.all().order_by('-f_group','f_step')
        # # page = int(request.GET.get('nowpage',1))
        # paginator = Paginator(qs,10) 
        # fList = paginator.get_page(nowpage)
        # context = {'fList':fList,'nowpage':nowpage,'countA':qs.count,'category':category,'searchword':searchword}
        # return render(request,'fList.html',context)
    # else:
        # category = request.POST.get('category')
        # searchword = request.POST.get('searchword')
    if category == 'first':
        qs = Fboard.objects.all().order_by('-f_group','f_step')
        # page = int(request.GET.get('nowpage',1))
        
    elif category == 'title':
        qs = Fboard.objects.filter(f_title__contains=searchword)
    elif category == 'content':
        qs = Fboard.objects.filter(f_content__contains=searchword)
    else:
        # a and b 
        # qs = Fboard.objects.filter(f_title__contains=searchword,f_content__contains=searchword)
        # a or b 
        qs = Fboard.objects.filter(Q(f_title__contains=searchword)|Q(f_content__contains=searchword))
        
        
    
    # qs = Fboard.objects.all().order_by('-f_group','f_step')
    # page = int(request.GET.get('nowpage',1))
    paginator = Paginator(qs,10) 
    fList = paginator.get_page(nowpage)
    context = {'fList':fList,'nowpage':nowpage,'countA':qs.count,'category':category,'searchword':searchword}

    print(category, searchword)
    
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
        category='first'
        searchword='first'
        return redirect('fboard:fList',nowpage,category,searchword)

def fView_old(request,nowpage,f_no):
    qs = Fboard.objects.get(f_no=f_no)
    qs.f_hit += 1
    qs.save()
    context = {'board':qs,'nowpage':nowpage}
    return render(request,'fView.html',context)

def fView(request,nowpage,category,searchword,f_no):
    qs = Fboard.objects.get(f_no=f_no)
    # 게시판리스트- f_group역순정렬, f_step순차정렬
    # qs = Fboard.objects.order_by('-f_group','f_step')
    # 이전글
    try:
        # 답글로 게시글이 등록될때 찾을수 있는 이전글검색
        qs_prev = Fboard.objects.filter(f_group=qs.f_group,f_step__lt=qs.f_step).order_by('-f_group','f_step').last().f_no
    except:  
        # 순차적으로 게시글이 등록될대 찾을수 있는 이전글검색
        try:
            qs_prev = Fboard.objects.filter(f_group__gt=qs.f_group).order_by('-f_group','f_step').last().f_no
        except:
            # 마지막 게시글 선택시 에러 처리
            qs_prev = Fboard.objects.order_by('-f_group','f_step').first().f_no
    
    # 다음글
    try:
        # 답글로 게시글이 등록될때 찾을수 있는 다음글검색
        qs_next = Fboard.objects.filter(f_group=qs.f_group,f_step__gt=qs.f_step).order_by('-f_group','f_step').first().f_no
    except:  
        # 순차적으로 게시글이 등록될대 찾을수 있는 다음글검색
        try:
            qs_next = Fboard.objects.filter(f_group__lt=qs.f_group).order_by('-f_group','f_step').first().f_no
        except:
            # 처음 게시글 선택시 에러 처리
            qs_next = Fboard.objects.order_by('-f_group','f_step').last().f_no
    
            
    print("qs_prev : ",qs_prev)
    qs.f_hit += 1
    qs.save()
    qsPrev = Fboard.objects.get(f_no=qs_prev)
    qsNext = Fboard.objects.get(f_no=qs_next)
    # 이전글 게시글 검색
    context={'board':qs,'boardPrev':qsPrev,'boardNext':qsNext,'nowpage':nowpage, 'category':category, 'searchword':searchword}
    return render(request,'fView.html',context)






def fReply(request,nowpage,f_no):
    if request.method == 'GET':
        qs = Fboard.objects.get(f_no=f_no)
        context = {'board': qs,'nowpage':nowpage}
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
        category='first'
        searchword='first'
        return redirect('fboard:fList',nowpage,category,searchword)
        # return redirect('fboard:fList',nowpage)

def fDelete(request,nowpage,f_no):
    qs = Fboard.objects.get(f_no=f_no)
    qs.delete()
    # return redirect('fboard:fList',nowpage)
    category='first'
    searchword='first'
    return redirect('fboard:fList',nowpage,category,searchword)


def fUpdate(request,nowpage,f_no):
    if request.method == 'GET':
        qs = Fboard.objects.get(f_no=f_no)
        context = {'board':qs,'nowpage':nowpage}
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
        category='first'
        searchword='first'
        return redirect('fboard:fList',nowpage,category,searchword)