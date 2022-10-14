from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from datetime import datetime


@receiver(user_logged_in)
def lastLogin(request,user,**kwargs):
    user.last_login = user.new_login
    user.new_login = datetime.now()
    user.save()
