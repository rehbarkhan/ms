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
class Index(View):

    @method_decorator(login_required)
    @method_decorator(dean_required)
    def get(self,request):
        return render(request,'dean/index.html',{})

class AdmissionApproval(View):

    @method_decorator(login_required)
    @method_decorator(dean_required)
    def get(self,request):
        user_names = CustomUser.object.filter(is_active = False)
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