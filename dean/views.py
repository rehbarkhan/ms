from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from dean.decorators import dean_required
from django.views import View


class Index(View):

    @method_decorator(login_required)
    @method_decorator(dean_required)
    def get(self,request):
        return render(request,'dean/index.html',{})
