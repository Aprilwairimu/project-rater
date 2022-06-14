from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns= [
    path('',views.home, name='home',),
    path('register',views.register, name='register',),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout,name='logout'),
    path('project/', views.project, name='project'),
    path('profile/',views.profile,name='profile'),
    path('profile/<username>/settings', views.edit_profile, name='edit'),
    path('search/', views.search_project, name='search'),
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)