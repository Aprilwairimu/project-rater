from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.



def home(request):
    return render(request,'home.html')

def register(request):
    return render(request,'register/register.html',)

def login(request):
    return render(request,'register/login.html')