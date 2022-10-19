from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class Index(View):
    
    def pageRouter(self,request):
        if request.user.is_authenticated:
            grp_type = request.user.groups.all()[0].name
            if 'admission' in grp_type:
                return redirect('admission:index')
            elif 'clg' in grp_type:
                return redirect('clgstaff:index')
            elif 'exam' in grp_type:
                return redirect('exam:index')
            elif 'finance' in grp_type:
                return redirect('finance:index')
            elif 'prof' in grp_type:
                return redirect('prof:index')
            elif 'site' in grp_type:
                return redirect('sitemanager:index')
            else:
                return redirect('student:index')
            


    def get(self,request):
        if request.user.is_authenticated:
            grp_type = request.user.groups.all()[0].name
            if 'admission' in grp_type:
                return redirect('admission:index')
            elif 'clg' in grp_type:
                return redirect('clgstaff:index')
            elif 'exam' in grp_type:
                return redirect('exam:index')
            elif 'finance' in grp_type:
                return redirect('finance:index')
            elif 'prof' in grp_type or 'dean' in grp_type:
                return redirect('prof:index')
            elif 'site' in grp_type:
                return redirect('sitemanager:index')
            else:
                return redirect('student:index')
        return render(request,'authsystem/index.html',{})
    
    def post(self,request):
        # Index.pageRouter(request)
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
                    return redirect('authsystem:authsystem_index')
        else:
            return redirect('authsystem:authsystem_index')

    
    
            


class Info(View):

    @method_decorator(login_required)
    def get(self,request):
        return render(request,'authsystem/info.html',{})

def user_logout(request):
    logout(request)
    return redirect('authsystem:authsystem_index')
