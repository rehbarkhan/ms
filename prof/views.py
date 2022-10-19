from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from prof.decoratos import prof_required
# Create your views here.

class Index(View):

    @method_decorator(login_required)
    @method_decorator(prof_required)
    def get(self,request):
        return render(request,'prof/index.html',{})
