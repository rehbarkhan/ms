from django.urls import path
from prof.views import Index
app_name = 'prof'

urlpatterns = [
    path('',Index.as_view(),name='index'),
]