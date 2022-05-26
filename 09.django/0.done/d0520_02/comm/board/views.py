from django.shortcuts import redirect, render
from board.models import Freeboard
# Create your views here.

def fWrite(request):
    
    if request.method == 'GET':
        return render(request,'fWrite.html')
    else:
        
        
        id = request.POST.get('id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        Freeboard.objects.create(id=id,f_title=title, f_content=content )
    
        return redirect('board:fList')

def fList(request):
    
    qs = Freeboard.objects.all()
    context = {"fList":qs}
    return render(request,'fList.html',context)


