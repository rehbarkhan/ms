from django.http import HttpResponse

def clg_staff_required(function):
    def wrapper_function(request,*args,**kwargs):
        if 'clg staff' in request.user.groups.all()[0].name:
            return function(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized to access this page <br><a href='/'>Return to main page</a>")
    return wrapper_function

def clg_staff_manager_required(function):
    def wrapper_function(request,*args,**kwargs):
        if 'clg staff manager' == request.user.groups.all()[0].name:
            return function(request,**args,**kwargs)
        else:
            return HttpResponse("You are not authorized to access this page <br><a href='/'>Return to main page</a>")
    return wrapper_function