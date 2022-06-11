from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .forms import RegisterForm,LoginForm
from urllib import request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import random

# Create your views here.



def home(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = PostForm()

    try:
        posts = Post.objects.all()
        posts = posts[::-1]
        a_post = random.randint(0, len(posts)-1)
        random_post = posts[a_post]
        print(random_post.photo)
    except Post.DoesNotExist:
        posts = None
    return render(request, 'home.html', {'posts': posts, 'form': form, 'random_post': random_post})

    
    

def logout(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("login")
    else:
        form = RegisterForm()
    return render(request,'register/register.html', {"form":form})

def login(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse('Such a user does not exist')
        else:
            return HttpResponse("Form is not Valid")
    return render(request,'register/login.html',{'form':form})

def profile(request, username):
    return render(request, 'profile.html')


def search_project(request):
    if request.method == 'GET':
        title = request.GET.get("title")
        results = Post.objects.filter(title__icontains=title).all()
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'searched.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'searched.html', {'message': message})