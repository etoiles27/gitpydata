from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse('할루')
    return render(request,'index.html')