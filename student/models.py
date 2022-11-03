from django.db import models 
from authsystem.models import CustomUser

# Course Model

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length = 255)
    duration = models.IntegerField()
    fee = models.DecimalField(max_digits = 10,decimal_places = 2)

    def __str__(self):
        return f"{self.name}, {self.fee} INR"

class CourseFee(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='Course')
    student = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='Student')
    date = models.DateField()
    ammount = models.DecimalField(max_digits = 10,decimal_places = 2)

    def __str__(self):
        return f"{self.student}"


class Student(models.Model):
    firstname = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255,blank=True)
    lastname = models.CharField(max_length=255)

    date_of_birth = models.DateField()
    mobile = models.CharField(max_length=10)
    emergency_mobile = models.CharField(max_length=10)
    
    present_address = models.CharField(max_length=255)
    present_city = models.CharField(max_length=255)
    present_state = models.CharField(max_length=255)
    present_zip = models.IntegerField()

    permanent_address = models.CharField(max_length=255)
    permanent_city = models.CharField(max_length=255)
    permanent_state = models.CharField(max_length=255)
    permanent_zip = models.IntegerField()

    course = models.ForeignKey(Course,on_delete = models.CASCADE,related_name = 'course')
    actual_fee = models.DecimalField(max_digits = 10, decimal_places =2)
    user = models.OneToOneField(CustomUser,null=True,blank=True,on_delete=models.CASCADE,related_name='studen_profile')
    def __str__(self):
        return f'{self.firstname} {self.lastname}'


