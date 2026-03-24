from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer
from .models import Employee
# Create your views here.
def home(request):
    return render(request,'employee/base.html')

class EmployeeList(APIView):
    def get(self,request):
        object = Employee.objects.all()
        serializer = EmployeeSerializer(object,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'success','data':serializer.data},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):
    def get_object(self,id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            raise Http404

    def get(self,request,id):
        employee = self.get_object(id)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        employee = self.get_object(id)
        serializer = EmployeeSerializer(employee,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'success','data':serializer.data},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        employee = self.get_object(id)
        employee.delete()
        return Response({'message':'success'},status=status.HTTP_204_NO_CONTENT)