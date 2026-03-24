from django.urls import path
from myapp import views
urlpatterns = [
    path("",views.home,name='home'),
    path('add-student/',views.add_student,name='add-student'),
    path('update-student/<int:id>/',views.update_student,name='update-student'),
]