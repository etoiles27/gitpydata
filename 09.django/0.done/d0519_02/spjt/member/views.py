from django.shortcuts import redirect, render
from member.models import Member
# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else :
        
        id = request.POST.get('m_id')
        pw = request.POST.get('m_pw')
        
        try:
            qs = Member.objects.get(m_id=id,m_pw=pw)
        except Member.DoesNotExist:
            qs = None
        
        
        
            
        if qs:            
            request.session['session_id']=qs.m_id
            request.session['session_name'] = qs.m_name
            request.session['msg'] = "정상적으로 로그인이 되었습니다."
            # redirect message 변수전달
            return redirect('/')
           
        else:
            msg='아이디 또는 패스워드가 일치하지 않습니다. 다시 로그인하세요.'
            return render(request,'login.html',{'message':msg})
                
                
        
def logout(request):
    request.session.clear()
    return redirect('/')
   

def memlist(request):
    qs = Member.objects.all()
    context = {"memberList":qs}
    
    return render(request,'list.html',context)