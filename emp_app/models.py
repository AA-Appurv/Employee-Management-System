from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=300, null=False)
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=300, null=False)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone}"