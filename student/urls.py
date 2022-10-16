from django.urls import path
from .views import StudentIndex

app_name = 'student'

urlpatterns = [
    path('',StudentIndex.as_view(),name='index')
]