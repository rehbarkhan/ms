from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from clgstaff.decorator import clg_staff_required,clg_staff_manager_required
class Index(View):

    @method_decorator(login_required)
    @method_decorator(clg_staff_required)
    def get(self,request):
        return render(request,'clgstaff/index.html',{})

