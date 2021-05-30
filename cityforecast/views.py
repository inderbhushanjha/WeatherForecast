import requests
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from decouple import config
from .models import Cities

# from django.db.models import Q  # for where clause queries.
# Create your views here.

API_KEY = config('WEATHER_API_open')


url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'

def homepage(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('home')
        else:
            messages.info(request, 'Incorrect Username or Password')
            return HttpResponseRedirect('login')

    return render(request,'login.html')

# logout function

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username = username).exists():  #check user already exists in the database.
            messages.info(request, 'Username Already Taken!')
            return HttpResponseRedirect('signup')
        if User.objects.filter(email = email).exists():
            messages.info(request, 'Email Already Taken!')
            return HttpResponseRedirect('signup')
        else:
            user = User.objects.create_user(username = username, password = password, email = email,first_name = first_name, last_name = last_name)
            user.save()
            return HttpResponseRedirect('login')

    return render(request, 'signup.html')

def home(request):
    if request.user.is_anonymous is not True:
        print("logged in")
        current_user = request.user
        citiesList = Cities.objects.filter(username_id = current_user) # creating current user object to get visited


        weatherList = []
        for city in citiesList:
            if requests.get(url.format(city, API_KEY)).status_code !=404:
                result = requests.get(url.format(city, API_KEY)).json()
                weatherdat = {
                    'city': result['name'],
                    'temperature' : result['main']['temp'],
                    'description' : result['weather'][0]['description'],
                    'icon' : result['weather'][0]['icon'],
                }
                weatherList.append(weatherdat)
        print(weatherList)
    else:
        return HttpResponseRedirect('homepage')

    return render(request, 'index.html', {'datas':weatherList[::-1]})

def about(request):
    return render(request, 'about.html')

def city(request):
    current_user = request.user
    if request.method == 'POST':
        city = request.POST['cityname']
        duplicateCityData = Cities.objects.filter(username_id = current_user ,visited = city).exists()
        if duplicateCityData is not True  and requests.get(url.format(city, API_KEY)).status_code !=404 :
            citydata = Cities(username_id = current_user.id,visited = city)  # adding city to database.
            citydata.save()
    return HttpResponseRedirect('home')


# def anonuser(request):
#     return render(request, 'index.html')