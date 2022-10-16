from django.http import HttpResponse

def student_access(function):
    def wrapper_funtion(request,*args,**kwargs):
        print("inside wrapper function")
        if request.user.groups.all()[0].name == 'student':
            print("inside the if of request")
            return function(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorize the access the page")
    return wrapper_funtion