from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from app1.form import*
from app1.models import *

def base(request):
    return render(request,'base.html')


def signup(request):
    if request.method == 'POST':
       
       username = request.POST['username']
       email =request.POST['email']
       password1 = request.POST['pass1']
       password2= request.POST['cpass2']
       if password1==password2:
                if User.objects.filter(username=username,email=email).exists():
                    messages.info(request, 'usename is exist ')
                    print("already have")
                else:
                    new_user=User.objects.create_user(username,email,password1)
                    new_user.save()
                    return redirect(user_login)
       else:
        print("wrong pass")
    return render(request,'signup.html')
        
def user_login(request):
    if request.method == 'POST':
        username =request.POST['username']
        password1 = request.POST['pass1']
        user = authenticate(request,username=username, password=password1)
        if user is not None:
            login(request,user)
            return redirect(base)
        else:
            messages.info(request,'user not exist')
            print('user not exist')
            return redirect(login)
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect(base)

def form1(request):
    form=studentform()
    if request.method =='POST':
        form=studentform(request.POST)
        if (form.is_valid()):
            form.save()
            return base (request)
    return render(request,'form1.html',{'form':form})
        