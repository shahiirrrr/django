from django.db import models

# Create your models here.


class student(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=25)
    def __str__(self):
        return self.name
