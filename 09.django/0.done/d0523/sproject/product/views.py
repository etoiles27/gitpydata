from django.shortcuts import redirect, render
from numpy import product
from product.models import Product
# Create your views here.

def pList(request):
    qs = Product.objects.all().order_by('-p_no')
    context = {'products':qs}
    return render(request,'pList.html',context)


def pIndex(request):
    qs = Product.objects.all()
    context = {'products':qs}
    return render(request,'pIndex.html',context)


def pView(request,p_no):
    qs = Product.objects.get(p_no=p_no)
    context = {'product':qs}
    return render(request,'pView.html',context)

def pWrite(request):
    if request.method == 'GET':
        return render(request, 'pWrite.html')
    else:
        
        
        name = request.POST.get('pName')
        serving = request.POST.get('pServing')
        price = request.POST.get('pPrice')
        content = request.POST.get('content')
        catego = request.POST.get('Pcategory')
        manuf = request.POST.get('pManu')
        punit = request.POST.get('pUnit')
        
        file=request.FILES.get('file',None)
       
  
    
        
        qs = Product(p_name=name,p_servings=serving,p_unitPrice=price,p_description=content,p_category=catego,p_manufacturer=manuf,p_unit=punit,p_fileName=file)
        qs.save()

        return redirect('product:pList')