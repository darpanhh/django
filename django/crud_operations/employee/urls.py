from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name = 'home'),
    path('employee/list',views.EmployeeList.as_view(),name='employee-list'),
    path('employee/<int:id>/',views.EmployeeDetail.as_view(),name='employee-detail')
]