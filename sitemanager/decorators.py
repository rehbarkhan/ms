from django.http import HttpResponse

def site_staff_requried(function):
    def wrapper_function(request,*args,**kwargs):
        if 'site staff' in request.user.groups.all()[0].name:
            return function(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized to access this page <br><a href='/'>Return to main page</a>")
    return wrapper_function


def site_staff_manager_required(function):
    def wrapper_function(request,*args,**kwargs):
        if 'site staff manager' == request.user.groups.all()[0].name:
            return function(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized to access this page <br><a href='/'>Return to main page</a>")
    return wrapper_function