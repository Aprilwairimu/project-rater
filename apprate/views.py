from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,JsonResponse
from .forms import RegisterForm,LoginForm,PostForm, UpdateUserForm, UpdateProfileForm, RateForm
from urllib import request
from django.contrib.auth.models import User
from .serializers import ProfileSerializer, UserSerializer
from django.contrib.auth import authenticate,login,logout
import random
from .models import Post,Rate,Profile
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view 
from rest_framework.response import Response
import json
from django.contrib.auth.decorators import login_required
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

    return render(request, 'home.html', { 'form': form,})

def logout(request):
    logout(request)
    return redirect('home')

# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


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

@login_required(login_url='login')
def project(request, post):
    post = Post.objects.get(title=post)
    rates = Rate.objects.filter(user=request.user, post=post).first()
    rate_status = None
    if rates is None:
        rate_status = False
    else:
        rate_status = True
    if request.method == 'POST':
        form = RatesForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.post = post
            rate.save()
            post_rates = Rate.objects.filter(post=post)

            design_rates = [d.design for d in post_rates]
            design_average = sum(design_rates) / len(design_rates)

            usability_rates = [us.usability for us in post_rates]
            usability_average = sum(usability_rates) / len(usability_rates)

            content_rates = [content.content for content in post_rates]
            content_average = sum(content_rates) / len(content_rates)

            score = (design_average + usability_average + content_average) / 3
            print(score)
            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.score = round(score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatesForm()
    params = {
        'post': post,
        'rate_form': form,
        'rate_status': rate_status

    }
    return render(request, 'project.html', params)

    
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