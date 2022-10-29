from django.urls import path
from finance.views import Index,FinanceProfile


app_name = 'finance'
urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('profile/',FinanceProfile.as_view(),name='profile'),
]