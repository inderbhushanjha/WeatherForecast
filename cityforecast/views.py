from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password = request.POST['password']
        print(uname)
        print(password)
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        fname = request.POST['fullname']
        email = request.POST['email']
        username = request.POST['username']
        p1 = request.POST['password1']
        p2 = request.POST['password2']
        tandc = request.POST['tc']
        
    return render(request, 'signup.html')

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')