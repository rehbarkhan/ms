from django.urls import path
from finance.views import Index,FinanceProfile,AccountProfile,StudentProfile


app_name = 'finance'
urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('profile/',FinanceProfile.as_view(),name='profile'),
    path('account/',AccountProfile.as_view(),name='account'),
    path('studentprofile/',StudentProfile.as_view(),name='studentprofile'),      
]