from django.shortcuts import render
from product.models import Product
# Create your views here.
def index(request):
    qs = Product.objects.all()
    context = {'products':qs}
    return render(request,'index.html',context)