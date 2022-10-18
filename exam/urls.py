from django.urls import path
from exam.views import Index

app_name = 'exam'

urlpatterns = [
    path('',Index.as_view(),name='index')
]