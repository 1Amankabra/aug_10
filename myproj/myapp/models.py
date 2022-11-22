from django.db import models

# Create your models here.
class Student(models.Model):
    firstname=models.CharField(max_length=30,blank=True)
    lastname=models.CharField(max_length=30)
    city=models.CharField(max_length=20)
    per=models.IntegerField()

    # def __str__(self):
    #  return self.firstname,self.lastname
    