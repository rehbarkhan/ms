from django.db import models

# Create your models here.


#Course
class Courses(models.Model):
    course_name = models.CharField(max_length=255)
    course_duration = models.IntegerField()
    course_ammount = models.DecimalField(decimal_places=2,max_digits=8)
    course_fee = models.DecimalField(decimal_places=2,max_digits=8)
    def __str__(self):
        return self.course_name


class StudentCourseFee(models.Model):
    total_fee = models.DecimalField(decimal_places=2,max_digits=8)
    fee_paid = models.DecimalField(decimal_places=2,max_digits=8)


"""
from django.db import models
from student.models import Courses,StudentCourseFee
from authsystem.models import CustomUser

#Creating model for registering a new memeber in admission department
class AdmissionDepart(models.Model):
    firstname = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255,blank=True)
    lastname = models.CharField(max_length=255)

    date_of_birth = models.DateField()
    mobile = models.IntegerField()
    emergency_mobile = models.IntegerField()
    
    present_address = models.CharField(max_length=255)
    present_city = models.CharField(max_length=255)
    present_state = models.CharField(max_length=255)
    present_zip = models.IntegerField()

    permanent_address = models.CharField(max_length=255)
    permanent_city = models.CharField(max_length=255)
    permanent_state = models.CharField(max_length=255)
    permanent_zip = models.IntegerField()

    #courses information  & finance information
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    discount_ammount = models.DecimalField(decimal_places=2,max_digits=8)
    

    #profile info & college info
    profile = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    finance_module = models.OneToOneField(StudentCourseFee,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.firstname}{self.lastname}'

    #creating the profile as well
    def save(self,*args,**kwargs):
        student_object = super().save(self,*args,**kwargs)
        st_id = student_object.id
        f_n = student_object.firstname
        l_n = student_object.lastname
        u_name = f'{f_n[:5].lower()}{l_n[5:].lower()}{st_id}'
        user_obj = CustomUser.object.create_user(username=u_name,password=f'{student_object.mobile}{student_object.date_of_birth.year}')
        

class StudentCourseFee(models.Model):
    total_fee = models.DecimalField(decimal_places=2,max_digits=8)
    fee_paid = models.DecimalField(decimal_places=2,max_digits=8)
"""