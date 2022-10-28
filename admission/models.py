from django.db import models
from django.forms import DateField
from authsystem.models import CustomUser

#Creating model for registering a new memeber in admission department
#Admission Staff Model


class AdmissionSalalry(models.Model):
    salary_date = DateField()
    salary_ammount = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f'self.id'
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
    account_type = models.CharField(default='',max_length=255)
    package_lpa = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    salary = models.ForeignKey(AdmissionSalalry,on_delete = models.CASCADE,null= True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True,related_name='admission')
    def __str__(self):
        return f'{self.firstname} {self.lastname}'


