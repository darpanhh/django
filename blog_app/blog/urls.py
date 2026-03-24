from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup,name='signup-page'),
    path('login/',views.loginn,name='login-page'),
    path('home/',views.home,name='home-page'),
    path('mypost/',views.myPost,name='my-post'),
    path('newpost/',views.newPost,name='new-post'),
    path('signout/',views.signout)
]
