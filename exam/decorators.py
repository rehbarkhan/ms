from django.http import HttpResponse


def exam_required(function):
    def wrapper_function(request,*args,**kwargs):
        if 'exam' in request.user.groups.all()[0].name:
            return function(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized to access this page <br><a href='/'>Return to main page</a>")
    return wrapper_function

def exam_manager_required(function):
    def wrapper_function(request,*args,**kwargs):
        if 'exam manager' == request.user.groups.all()[0].name:
            return function(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized to access this page <br><a href='/'>Return to main page</a>")
    return  wrapper_function