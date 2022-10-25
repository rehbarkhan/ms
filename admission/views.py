from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from admission.decorators import admission_required,admission_manager_requried

class Index(View):
    @method_decorator(login_required)
    @method_decorator(admission_required)
    def get(self,request):
        return render(request,'admission/index.html',{})

class Account(View):
    @method_decorator(login_required)
    @method_decorator(admission_manager_requried)
    def get(self,request):
        return render(request,'admission/account.html',{})


class Finance(View):
    @method_decorator(login_required)
    @method_decorator(admission_required)
    def get(self,request):
        return render(request,'admission/finance.html',{})

class Profile(View):
    @method_decorator(login_required)
    @method_decorator(admission_required)
    def get(self,request):
        return render(request,'admission/profile.html',{})

class StudentProfile(View):
    @method_decorator(login_required)
    @method_decorator(admission_required)
    def get(self,request):
        return render(request,'admission/studentprofile.html',{})
