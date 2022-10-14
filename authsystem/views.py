from django.shortcuts import render


def index(request):
    # a = 'My Name is Rehbar'
    return render(request,'index.html',{})
