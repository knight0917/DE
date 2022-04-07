from distutils.log import error
from django.shortcuts import redirect, render 
from home.models import UserDetail
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

# Create your views here.

def home(request):
    return render(request, 'home.html')
   
def registerPage(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration...')
            
    return render(request, 'register.html', {'form':form})

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method =='POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!!!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User does not exist!!!')

    return render(request, 'register.html', {'page':page})

def logoutUser(request):
    logout(request)
    return redirect('home')

def about(request):
    return render(request, 'about.html')

def template(request):

    if request.method == 'POST':
        
        nm     = request.POST.get('name')
        eml    = request.POST.get('email')
        adrs   = request.POST.get('address')
        ph     = request.POST.get('phone')
        wb     = request.POST.get('web')
        lkdn   = request.POST.get('linkedin')
        gthb   = request.POST.get('github')
        acdql  = request.POST.get('acadqual')
        wrkex  = request.POST.get('workexp')
        inter  = request.POST.get('inter')
        about  = request.POST.get('about')

        data = UserDetail(name=nm, email=eml, address=adrs, phone=ph, web=wb, linkedin=lkdn, github=gthb, acadqual=acdql, workexp=wrkex, inter=inter, about=about)
        data.save()

        return redirect('userdata/')
    else:
        return render(request, 'template.html')

def temp1(request):
    userdetail = UserDetail.objects.last()
    return render(request, 'temp1.html', {'userdetail':userdetail})



