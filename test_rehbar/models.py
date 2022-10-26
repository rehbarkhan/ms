from django.db import models

# Create your models here.

class DT(models.Model):
    date = models.DateField()

    def __str__(self):
        return f'{self.date}'

class Name(models.Model):
    name = models.CharField(max_length=255)
    date = models.ForeignKey(DT,on_delete=models.CASCADE,related_name='DT')

    def __str__(self):
        return self.name
