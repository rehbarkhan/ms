from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from dean.decorators import dean_required
from django.views import View
from admission.models import AdmissionDepart
from authsystem.models import CustomUser
from django.contrib import messages
from student.forms import CourseForm
from student.models import Course
from django.db.models import Q
from dean.forms import DeanDepartmentForm
from django.contrib.auth.models import Group
class Index(View):

    @method_decorator(login_required)
    @method_decorator(dean_required)
    def get(self,request):
        return render(request,'dean/index.html',{})

class AdmissionApproval(View):

    @method_decorator(login_required)
    @method_decorator(dean_required)
    def get(self,request):
        user_names = CustomUser.object.filter(Q(is_active = False) & Q(groups__name__in=['admission','admission manager']))
        admission_list = []
        for f in user_names:
            admission = AdmissionDepart.objects.get(user = f)
            admission_list.append(admission)
        return render(request,'dean/admission_approve.html',{'user_names':admission_list})

class AdmissinApprovalLink(View):

    @method_decorator(login_required)
    @method_decorator(dean_required)
    def get(self,request,u_name):
        user_object = CustomUser.object.get(username = u_name)
        if user_object.is_active == False:
            user_object.is_active = True
            user_object.save()
            messages.success(request,"Profile approved successfully.")
            return redirect('dean:admission')
        else:
            messages.info(request,"Profile is already approved successfully.")
            return redirect('dean:admission')


class CourseDetails(View):

    @method_decorator(login_required)
    @method_decorator(dean_required)
    def get(self,request):
        courses = Course.objects.all()
        form = CourseForm()
        return render(request,'dean/course.html',{'courses':courses,'form':form})
    
    def post(self,request):
        form_data = CourseForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Course Added Successfully")
        else:
            messages.error(request,"Unable to add course")
        
        return redirect('dean:course')
    
class FinanceApprove(View):

    @method_decorator(login_required)
    @method_decorator(dean_required)
    def get(self,request):
        user_names = CustomUser.object.filter(Q(is_active = 0) & Q(groups__name__in=['finance','finance manager']))
        return render(request,'dean/financeapproval.html',{'user_names':user_names})
class FinanceApproval(View):
    @method_decorator(login_required)
    @method_decorator(dean_required)
    def get(self,request,pk):
        try:
            user_name = CustomUser.object.get(pk=pk)
            user_name.is_active = True
            user_name.save()
            messages.success(request,'Profile Activate Successfully')
        except:
            messages.error(request,'Unable to Activate Profile')
        return redirect('dean:financestaff')

class EditCourse(View):
    @method_decorator(login_required)
    @method_decorator(dean_required)
    def get(self,request,pk):
        try:
            data = Course.objects.get(pk=pk)
        except:
            data = None
        return render(request,'dean/editcourse.html',{'data':data})

    
    @method_decorator(login_required)
    @method_decorator(dean_required)
    def post(self,request,pk):
        course_name = request.POST.get('course-name',None)
        course_duration = request.POST.get('course-duration',None)
        course_description = request.POST.get('course-description',None)
        course_fee = request.POST.get('course-fee',None)

        if course_name and course_duration and course_description and course_fee:
            try:
                course_details = Course.objects.get(pk=pk)
                course_details.name = course_name
                course_details.description = course_description
                course_details.duration = course_duration
                course_details.fee = course_fee
                course_details.save()
                return redirect('dean:course')
            except:
                return redirect('dean:course')
        else:
            return redirect('dean:course')


class DeanNewStaff(View):
    
    @method_decorator(login_required)
    @method_decorator(dean_required)
    def get(self,request):
        form = DeanDepartmentForm()
        return render(request,'dean/newstaff.html',{'form':form})

    @method_decorator(login_required)
    @method_decorator(dean_required)
    def post(self,request):
        form_data = DeanDepartmentForm(request.POST)
        if form_data.is_valid():
            form_object = form_data.save()
            f_name = form_object.firstname
            l_name = form_object.lastname
            i_name = form_object.id
            mob = form_object.mobile
            dob = form_object.date_of_birth.year
            user_object = CustomUser.object.create_user(
                username=f'{f_name[:5].lower()}{l_name[:5].lower()}d{i_name}',
                password = f'{str(mob)[:5]}@{dob}',
                is_active = True
            )
            user_object.groups.add(Group.objects.get(name='dean'))
            form_object.user = user_object
            form_object.account_type = 'dean'
            form_object.save()
            messages.success(request,f'Profile created successfully : username {f_name[:5].lower()}{l_name[:5].lower()}d{i_name}')
        else:
            print("something is wrong")
        return redirect('dean:staff')