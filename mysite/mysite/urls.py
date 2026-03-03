"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import *
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import home



urlpatterns = [
    path('admin/', admin.site.urls),
    path('set-cookie/',set_cookie),
    path('get-cookie/',get_cookie),
    path('get-session/',get_session),
    path('set-session/',set_session),
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view()),
    path('dashboard/',dashboard),
    path('',home),
]
