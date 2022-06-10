from django.shortcuts import render
from django.http  import HttpResponse,Http404

# Create your views here.



def home(request):
    return render(request,'home.html')

def register(request):
    return render(request,'register/register.html',)

def login(request):
    return render(request,'register/login.html')