from django.db import models
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=155)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField ( upload_to='pictures/',null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

class Rate(models.Model):
    rate = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )

    design = models.IntegerField(choices=rate,default=0,blank=True)
    Usability  = models.IntegerField(choices=rate,blank=True)
    content = models.IntegerField(choices=rate,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings', null=True)

    def save_rate(self):
        self.save()
    
    
class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=300, null=True, blank=True)
    # posted_projects
    name = models.CharField(blank=True, max_length=120)
    contact = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.name} Profile'

    @classmethod
    def get_rate(cls, id):
        rates = Rate.objects.filter(post_id=id).all()
        return rates

    def __str__(self):
        return f'{self.post} Rate'



    @classmethod
    def search_project(cls,title):
        project = cls.objects.filter(title__icontains=title).all()
        return project
    

    @classmethod
    def all_posts(cls):
        return cls.objects.all()




   