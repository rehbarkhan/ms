from django.http import HttpResponse

def student_access(function):
    def wrapper_funtion(request,*args,**kwargs):
        print("inside wrapper function")
        if request.user.groups.all()[0].name == 'student':
            return function(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized to access this page <br><a href='/'>Return to main page</a>")
    return wrapper_funtion