from django.db import models

# Create your models here.
class Studentdata1(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    add=models.CharField(max_length=50)
    gpa=models.FloatField()
    college=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name