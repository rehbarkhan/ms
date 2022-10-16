from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from student.decorators import student_access
class StudentIndex(View):
    
    @method_decorator(login_required)
    @method_decorator(student_access)
    def get(self,request):
        return render(request,'student_index.html',{})