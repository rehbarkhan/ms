from django.urls import path
from authsystem.views import Index,Info,user_logout

app_name='authsystem'

urlpatterns = [
    path('', Index.as_view(), name='authsystem_index'),
    path('info/',Info.as_view(),name='authsystem_info'),
    path('logout/',user_logout,name='authsystem_logout')
]