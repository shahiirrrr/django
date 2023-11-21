from django.db import models

# Create your models here.


class doctor(models.Model):
    docid=models.IntegerField()
    name=models.CharField(max_length=20)
    section=models.CharField(max_length=25)
    def __str__(self):
        return self.name