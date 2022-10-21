from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser,PermissionsMixin,BaseUserManager)

class CustomBaseManager(BaseUserManager):

    def create_user(self,username,password=None,**kwargs):
        user = self.model(username=username,**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,password=None,**kwargs):
        superuser = self.model(username=username,**kwargs)
        superuser.set_password(password)
        superuser.is_active = True
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save(using = self._db)
        return superuser

class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(unique=True,max_length=255)
    password = models.CharField(max_length=255)
    account_created_date = models.DateTimeField(auto_now_add = True)
    new_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    object = CustomBaseManager()
