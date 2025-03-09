from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth import logout
from django.db import models
from blog.views import post_list as ps
from django.contrib import messages

# Create your views here.


def load_user_login(request):
    print("load_user_login called")
    return render(request, 'user/login.html')

def user_logout(request):
    if request.user.is_authenticated:
        messages.success(request, "successfully logged out")
        print("successfully logged out")
        logout(request)
    else:
        messages.error(request, "already logged out")
        print("logging out failed")

    return ps(request)

def user_login(request):
    print("user login called")
    if request.method == 'POST':
        print("POST called")
        user_name = request.POST.get('username')
        user_pwd = request.POST.get('password')
        print(f"auth info is [{user_name}] [{user_pwd}]")
        
        user = authenticate(request, username=user_name, password=user_pwd)

        if user is None:
            messages.error(request, "check id or pwd")
        else:
            login(request, user)

        return ps(request)

    elif request.method == 'GET':
        print("GET called")
        load_user_login(request)
        return render(request, 'user/login.html')

    else:
        print("method not found")
        return None