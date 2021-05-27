from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('home',views.home,name='signup'),
    path('about',views.about,name='signup'),
]
