from django.db import models
from authsystem.models import CustomUser

# Create your models here.


class DeanSalary(models.Model):
    salary_date = models.DateField()
    salary_ammount = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f'self.id'


class DeanDepartment(models.Model):
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
    account_type = models.CharField(default='dean',max_length=255)
    package_lpa = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    salary = models.ForeignKey(DeanSalary,on_delete = models.CASCADE,null= True,related_name='dean_salary')
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True,related_name='dean')
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
