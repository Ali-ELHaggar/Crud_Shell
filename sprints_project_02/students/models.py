from django.db import models

# Create your models here.

class Student(models.Model):
    f_name = models.CharField(max_length=255, null=True)
    I_name = models.CharField(max_length=255, null=True)
