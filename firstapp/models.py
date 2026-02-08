from django.db import models

# Create your models here.
class Student(models.Model):
    ename=models.CharField(max_length=50)
    eage=models.IntegerField()
    eadd=models.CharField(max_length=50)
    erank=models.IntegerField()
    ecollege=models.CharField(max_length=50)
    ephno=models.IntegerField()

    def __str__(self):
        return self.ename  # Return name as string




