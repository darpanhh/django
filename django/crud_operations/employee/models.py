from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    salary = models.IntegerField()
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
