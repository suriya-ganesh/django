from django.db import models
from django.contrib.auth.models import User


# # Create your models here.
# class Log(models.Model):
#     Name= models.CharField(max_length=50)
#     Phone_number= models.CharField(max_length=10)
#
#     def __str__(self):
#         return self.Name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name