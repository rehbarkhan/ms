from django.http import HttpResponse


def finance_required(function):
    def wrapper_function(request,*args,**kwargs):
        if 'finance' in request.user.groups.all()[0].name:
            return function(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized to access this page <br><a href='/'>Return to main page</a>")
    return wrapper_function

def finance_manager_required(function):
    def wrapper_function(request,*args,**kwargs):
        if 'finance manager' == request.user.groups.all()[0].name:
            return function(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized to access this page <br><a href='/'>Return to main page</a>")
    return wrapper_function