from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class Index(View):
    def get(self,request):
        return render(request,'authsystem/index.html',{})
    
    def post(self,request):
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        nextpage = request.POST.get('next',None)
        if username is not None and password is not None:
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                if nextpage:
                    return redirect(nextpage)
                else:
                    return redirect('authsystem:authsystem_info')
        else:
            return redirect('authsystem:authsystem_index')


class Info(View):

    @method_decorator(login_required)
    def get(self,request):
        return render(request,'authsystem/info.html',{})

def user_logout(request):
    logout(request)
    return redirect('authsystem:authsystem_index')
