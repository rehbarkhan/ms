from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from sitemanager.decorators import site_staff_manager_required,site_staff_requried
# Create your views here.

class Index(View):

    @method_decorator(login_required)
    @method_decorator(site_staff_requried)
    def get(self,request):
        return render(request,'sitemanager/index.html',{})
