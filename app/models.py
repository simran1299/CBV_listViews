from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=100)
    princlpal=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class Student(models.Model):
    Name=models.CharField(max_length=100)
    age=models.IntegerField()
    School_name=models.ForeignKey(School, on_delete=models.CASCADE,related_name='student')

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.Name

