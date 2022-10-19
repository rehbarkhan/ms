from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from admission.decorators import admission_required

class Index(View):

    @method_decorator(login_required)
    @method_decorator(admission_required)
    def get(self,request):
        return render(request,'admission/index.html',{})
