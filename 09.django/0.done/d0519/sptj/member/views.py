from django.shortcuts import redirect, render
from member.models import Member
# Create your views here.


def mlist(request):
    qs=Member.objects.order_by('-m_no')
    context = {'memberList':qs}
    return render(request,'list.html',context)



def login(request):
    if request.method == 'GET':
        print('login get 호출')
        return render(request,'login.html')
        
    else:
        print('login post 호출')
        id = request.POST.get('m_id')
        pw = request.POST.get('m_pw')
        
        try:
            qs = Member.objects.get(m_id=id,m_pw=pw)
        except Member.DoesNotExist:
            qs = None
            
            
        if qs:
            request.session['session_id'] = qs.m_id
            request.session['session_name'] = qs.m_name
            return redirect('/',message='성공!')
        else:
            msg = '아이디 또는 패스워드가 일치하지 않습니다. '
            return render(request,'login.html',{'message':msg})
        
def logout(request):
    request.session.clear()
    # del request.session['session_id']
    return redirect('/')