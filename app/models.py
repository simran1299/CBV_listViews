from django.db import models

# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=100)
    princlpal=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    Name=models.CharField(max_length=100)
    age=models.IntegerField(max_length=100)
    School_name=models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

