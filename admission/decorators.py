from django.http import HttpResponse

def admission_required(function):
    def wrapper_function(request,*args,**kwargs):
        if 'admission' in request.user.groups.all()[0].name:
            return function(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized to access this page <br><a href='/'>Return to main page</a>")
    return wrapper_function

def admission_manager_requried(function):
    def wrapper_function(request,*args,**kwargs):
        if 'admission manager' == request.user.groups.all()[0].name:
            return function(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized to access this page <br><a href='/'>Return to main page</a>")
    return wrapper_function
