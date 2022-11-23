from django.contrib import messages
from django.shortcuts import render,redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from admission.decorators import admission_required,admission_manager_requried
from admission.forms import AdmissionDepartmentForm
from authsystem.models import CustomUser
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login
from student.forms import StudentForm

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
                username=f'{f_name[:5].lower()}{l_name[:5].lower()}{i_name}',
                password = f'{str(mob)[:5]}@{dob}',
            )
            user_object.groups.add(Group.objects.get(name=form_data.account_type))
            form_object.user = user_object
            form_object.save()
            messages.success(request,f'Profile created successfully : username {f_name[:5].lower()}{l_name[:5].lower()}{i_name}')
        else:
            print("something is wrong")
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
        form = StudentForm()
        return render(request,'admission/studentprofile.html',{'form':form})

    @method_decorator(login_required)
    @method_decorator(admission_required)
    def post(self,request):
        form_data = StudentForm(request.POST)
        print('got the data')
        if form_data.is_valid():
            form_object = form_data.save()
            print('data saved')
            f_name = form_object.firstname
            l_name = form_object.lastname
            i_name = form_object.id
            mob = form_object.mobile
            dob = form_object.date_of_birth.year
            user_object = CustomUser.object.create_user(
                username=f'{f_name[:5].lower()}{l_name[:5].lower()}s{i_name}',
                password = f'{str(mob)[:5]}@{dob}'
            )
            print('profile creatd')
            user_object.groups.add(Group.objects.get(name='student'))
            print("group added")
            form_object.user = user_object
            form_object.save()
            print("Profiel saved")
            messages.success(request,f'Student profile created successfully : username {f_name[:5].lower()}{l_name[:5].lower()}s{i_name}')
        else:
            print("something is wrong")
        return redirect('admission:student-profile')

class AdmissionProfilePasswordReset(View):
    @method_decorator(login_required)
    @method_decorator(admission_required)
    def post(self,request):
        old_password = request.POST.get('old_password',None)
        new_password = request.POST.get('new_password',None)
        if old_password is not None and new_password is not None:
            user_id = authenticate(username=request.user.username,password=old_password)
            if user_id is not None:
                user_id.set_password(new_password)
                user_id.save()
                login(request,user_id)
                messages.success(request,'Password changed successfully')
            else:
                messages.error(request,'Failed to change the password, try again')
        return redirect('admission:profile')
        
