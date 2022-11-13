from django.shortcuts import render,redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from finance.decorators import finance_required,finance_manager_required
from student.models import Student,CourseFee
from django.db.models import Q
from authsystem.models import CustomUser
from finance.forms import FinanceForm
from django.contrib.auth.models import Group
from django.contrib import messages
from datetime import datetime
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
        student_names = CustomUser.object.filter(Q(is_active = False) & Q(groups__name='student'))
        return render(request,'finance/studentprofile.html',{'students':student_names}) 
    
class StudentActivate(View):
    @method_decorator(login_required)
    @method_decorator(finance_required)
    def get(self,request,pk):
        user_data = CustomUser.object.get(pk=pk)
        fee_details = CourseFee.objects.filter(student=user_data)
        total_fee = 0
        if fee_details.exists:
            for fee in fee_details:
                total_fee += fee.ammount
        return render(request,'finance/student_pay.html',{'user_data':user_data,'fee_paid':total_fee})


class AcceptFee(View):

    @method_decorator(login_required)
    @method_decorator(finance_required)
    def post(self,request):
        id = request.POST.get('id',None)
        fee = request.POST.get('fee',None)
        if id is not None and fee is not None:
            try:
                user_data = CustomUser.object.get(pk=id)
            except:
                messages.error(request,'Error')

            fee_object = CourseFee(student=user_data,date=datetime.now(),ammount=fee)
            fee_object.save()
            if user_data.is_active == 0:
                user_data.is_active = 1
                user_data.save()
            messages.success(request,'Data Saved Successfully')    

        return redirect('finance:studentactivate',pk=id)


class SearchStudent(View):
    def post(self,request):
        search_data = request.POST.get('search',None)
        data = Student.objects.filter(Q(firstname__in=search_data.split())| Q(lastname__icontains=search_data) | Q(id__icontains = search_data.split()) | Q(mobile = search_data) | Q(user__username__icontains=search_data))
        return render(request,'finance/student_search.html',{'data':data})