from django.urls import path
from . import views


urlpatterns= [
    path('',views.home, name='home',),
    path('register',views.register, name='register',),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    # path('project/<post>', views.project, name='project'),
    path('search/', views.search_project, name='search'),
]