from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField ( upload_to='pictures/',null=True, blank=True)
    description = models.CharField(max_length=300,null=True, blank=True)

class Profile(models.Model):
    prof_pic =  models.ImageField (null=False, blank=False)
    bio = models.TextField(max_length=100, null=True, blank=True)
    # posted_projects
    # contact