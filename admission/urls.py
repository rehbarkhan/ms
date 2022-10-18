from django.urls import path
from admission.views import Index
app_name = 'admission'
urlpatterns = [
    path('',Index.as_view(),name='index')
]
