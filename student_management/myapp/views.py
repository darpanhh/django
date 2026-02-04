from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from myapp.models import Student
from myapp.forms import StudentForm

# Create your views here.

@login_required(login_url="/account/login/")
def home(request):
    students = Student.objects.all()
    return render(request,'index.html',{'students':students})

@login_required(login_url="/account/login/")
def add_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    return render(request,'add_student.html',{'form':form})

@login_required(login_url="/account/login/")
def update_student(request,id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    return render(request,'update_student.html',{'form':form})












