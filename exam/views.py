from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from exam.decorators import exam_manager_required,exam_required
class Index(View):

    @method_decorator(login_required)
    @method_decorator(exam_required)
    def get(self,request):
        return render(request,'exam/index.html',{})