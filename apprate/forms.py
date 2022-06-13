from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.forms import ModelForm,widgets
from .models import *





class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class LoginForm(forms.Form):
    email=forms.CharField(max_length=50)
    password=forms.CharField(max_length=20, widget=forms.PasswordInput)

class PostForm(forms.ModelForm):
   
    class Meta:
        model = Post
        fields = ('__all__')

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','profile_picture', 'bio', 'contact']

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['design', 'Usability', 'content']

   