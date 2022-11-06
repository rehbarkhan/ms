from django.urls import path
from finance.views import Index,FinanceProfile,AccountProfile,StudentProfile,StudentActivate


app_name = 'finance'
urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('profile/',FinanceProfile.as_view(),name='profile'),
    path('account/',AccountProfile.as_view(),name='account'),
    path('studentprofile/',StudentProfile.as_view(),name='studentprofile'),
    path('studentactivate/<int:pk>/',StudentActivate.as_view(),name='studentactivate'),   
]