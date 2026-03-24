from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import models
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        newUser = User.objects.create_user(username=name, email=email, password=password)
        newUser.save()
        return redirect('/login')
    return render(request, 'blog/signup.html')


def loginn(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            return redirect('/login')
    return render(request, 'blog/login.html')


def home(request):
    context = {
        'posts': Posts.objects.all().order_by('-date_posted')
    }
    return render(request, 'blog/home.html', context)


@login_required(login_url='/login')
def newPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        npost = models.Posts(title=title, content=content, author=request.user)
        npost.save()
        return redirect('/mypost')
    return render(request, 'blog/newpost.html')


@login_required(login_url='/login')
def myPost(request):
    context = {'posts': Posts.objects.filter(author=request.user).order_by('-date_posted')}
    return render(request, 'blog/mypost.html', context)


@login_required(login_url='/login')
def updatePost(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    # Only the author can update
    if post.author != request.user:
        return redirect('/home')
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('/mypost')
    return render(request, 'blog/editpost.html', {'post': post})


@login_required(login_url='/login')
def deletePost(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    # Only the author can delete
    if post.author != request.user:
        return redirect('/home')
    if request.method == 'POST':
        post.delete()
        return redirect('/mypost')
    return render(request, 'blog/deletepost.html', {'post': post})


def signout(request):
    logout(request)
    return redirect('/login')
