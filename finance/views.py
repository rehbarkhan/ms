from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from finance.decorators import finance_required,finance_manager_required
from student.models import Student
from django.db.models import Q
from authsystem.models import CustomUser
from django.http import HttpResponse
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
        # fetching all the student object who are not yet active
        user_name = CustomUser.object.filter(Q(is_active = False) & Q(groups__name='student'))
        print(user_name)
        student_list = []
        for f in user_name:
            print(f)
            student = Student.objects.get(user = f)
            student_list.append(student)
        return render(request,'finance/studentprofile.html',{'students':student_list}) 
    
class StudentActivate(View):
    @method_decorator(login_required)
    @method_decorator(finance_required)
    def get(self,request,pk):
        return render(request,'finance/student_pay.html',{})