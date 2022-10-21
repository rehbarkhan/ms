from django.core.management.base import BaseCommand
from authsystem.models import CustomUser
from django.contrib.auth.models import Group

class Command(BaseCommand):
    def handle(self,*args,**kwargs):
        print("*************** Setting up the initial DB settings *********")
        print(" - Adding Group to the Database -")
        group_list = [
            "dean","prof","exam","exam manager","admission","admission manager",
            "site staff","site staff manager","finance","finance manager", "student","clg staff","clg staff manager"
        ]
        for x in group_list:
            Group.objects.create(name=x)
            print(f"  - Group created for {x.title()} successfully")
        print(' - Adding Group Completed - ')

        user_auth_list = [
            "dean","exam manager","admission manager",
            "site staff manager","finance manager","clg staff manager"
        ]

        print(" - Adding Superuser Profile for internal user - ")
        for x in user_auth_list:
            obj = CustomUser.object.create_superuser(username=x,password='Welcome@1234')
            obj.groups.add(Group.objects.get(name=x))
            obj.save()
            print(f"  - Username : {x} - Password : 'Welcome@1234' created successfully")
        print("*************** DB Setting Completed *********")
