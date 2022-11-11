from django.shortcuts import render,redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from finance.decorators import finance_required,finance_manager_required
from student.models import Student
from django.db.models import Q
from authsystem.models import CustomUser
from finance.forms import FinanceForm
from django.contrib.auth.models import Group
from django.contrib import messages
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
    @method_decorator(finance_manager_required)
    def get(self,request):
        form = FinanceForm()
        return render(request,'finance/Account.html',{'form':form})

    @method_decorator(login_required)
    @method_decorator(finance_manager_required)
    def post(self,request):
        form_data = FinanceForm(request.POST)
        if form_data.is_valid():
            form_object = form_data.save()
            f_name = form_object.firstname
            l_name = form_object.lastname
            i_name = form_object.id
            mob = form_object.mobile
            dob = form_object.date_of_birth.year
            user_object = CustomUser.object.create_user(
                username=f'{f_name[:5].lower()}{l_name[:5].lower()}f{i_name}',
                password = f'{str(mob)[:5]}@{dob}'
            )
            user_object.groups.add(Group.objects.get(name=form_object.account_type))
            form_object.user = user_object
            form_object.save()
            messages.success(request,f'Profile created successfully : username {f_name[:5].lower()}{l_name[:5].lower()}f{i_name}')
        else:
            print("something is wrong")
        return redirect('finance:account')

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