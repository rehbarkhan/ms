from  django.urls import path
from clgstaff.views import Index

app_name = 'clgstaff'

urlpatterns = [
    path('',Index.as_view(),name='index')
]