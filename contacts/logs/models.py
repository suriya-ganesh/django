from django.db import models

# Create your models here.
class Log(models.Model):
    Name= models.CharField(max_length=50)
    Phone_number= models.CharField(max_length=10)

    def __str__(self):
        return self.Name

