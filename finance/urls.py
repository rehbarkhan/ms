from django.urls import path
from finance.views import Index

app_name = 'finance'
urlpatterns = [
    path('',Index.as_view(),name='index')
]