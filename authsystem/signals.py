from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.dispatch import receiver
from datetime import datetime


@receiver(user_logged_in)
def firstLogin(request,user,**kwargs):
    request.session['last_stamp'] = str(user.new_login)
    user.new_login = datetime.now()
    user.save()

# @receiver(user_logged_out)
# def lastLogin(request,user,**kwargs):
#     user.last_login = user.new_login
#     user.save()