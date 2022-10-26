from django.shortcuts import render,redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from admission.decorators import admission_required,admission_manager_requried
from admission.forms import AdmissionDepartmentForm
from authsystem.models import CustomUser
from django.contrib.auth.models import Group

class Index(View):
    @method_decorator(login_required)
    @method_decorator(admission_required)
    def get(self,request):
        return render(request,'admission/index.html',{})

class Account(View):
    @method_decorator(login_required)
    @method_decorator(admission_manager_requried)
    def get(self,request):
        form = AdmissionDepartmentForm()
        return render(request,'admission/account.html',{'form':form})

    @method_decorator(login_required)
    @method_decorator(admission_manager_requried)
    def post(self,request):
        form_data = AdmissionDepartmentForm(request.POST)
        if form_data.is_valid():
            form_object = form_data.save()
            f_name = form_object.firstname
            l_name = form_object.lastname
            i_name = form_object.id
            mob = form_object.mobile
            dob = form_object.date_of_birth.year
            user_object = CustomUser.object.create_user(
                username=f'{f_name[:5].lower()}{l_name[5:].lower()}{i_name}',
                password = f'{str(mob)[:5]}@{dob}'
            )
            user_object.groups.add(Group.objects.get(name=form_object.account_type))
            form_object.user = user_object
            form_object.save()
        return redirect('admission:account')





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
