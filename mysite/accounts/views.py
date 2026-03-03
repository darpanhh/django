from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.

def set_cookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('username','darpan',max_age=30)
    return response

def get_cookie(request):
    username = request.COOKIES.get('username')
    return HttpResponse(f"Username : {username}")

def set_session(request):
    request.session['username'] = 'darpan'
    return HttpResponse("Session set")

def get_session(request):
    username = request.session.get('username')
    return HttpResponse(f'Username: {username}')

# from django.shortcuts import render

def home(request):
    return render(request, "accounts/home.html")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    return Response({"message": "Welcome Darpan"})