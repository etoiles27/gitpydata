from django.shortcuts import render

# Create your views here.

def memberList(request):
    return render(request,'memberList.html')

def login(request):
    return render(request,'login.html')


def list(request):
    return render(request,'list.html')