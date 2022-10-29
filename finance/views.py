from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from finance.decorators import finance_required,finance_manager_required

class Index(View):
    @method_decorator(login_required)
    @method_decorator(finance_required)
    def get(self,request):
        return render(request,'finance/base.html',{})

class FinanceProfile(View):
    @method_decorator(login_required)
    @method_decorator(finance_required)
    def get(self,request):
        return render(request,'finance/profile.html',{})

class AccountProfile(View):
    @method_decorator(login_required)
    @method_decorator(finance_required)
    @method_decorator(finance_manager_required)
    def get(self,request):
        return render(request,'finance/Account.html',{})        

class StudentProfile(View):
    @method_decorator(login_required)
    @method_decorator(finance_required)
    def get(self,request):
        return render(request,'finance/studentprofile.html',{}) 