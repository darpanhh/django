from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from account.forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
    return render(request,'register.html',{'form':form})

def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username= username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')

    return render(request,'login.html',{'form':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/account/login/')