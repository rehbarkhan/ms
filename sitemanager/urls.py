from django.urls import path
from sitemanager.views import Index

app_name = 'sitemanager'

urlpatterns = [
    path('',Index.as_view(),name='inde')
]
