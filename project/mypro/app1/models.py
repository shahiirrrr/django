from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    pdf=models.FileField(upload_to='book/pdf')
    covor=models.ImageField(upload_to='book/cover',null=True,blank=True)
    