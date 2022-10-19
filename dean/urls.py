from django.urls import path
from dean.views import Index
app_name = 'dean'

urlpatterns = [
    path('',Index.as_view(),name='index')
]