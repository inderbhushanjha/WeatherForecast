from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('home',views.home,name='signup'),
    path('about',views.about,name='signup'),
    path('logout', views.logout, name='logout'),
    path('city', views.city, name='city'),
    path('homepage', views.homepage, name='city')
]

