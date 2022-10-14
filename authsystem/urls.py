from django.urls import path
from authsystem.views import index

app_name='authsystem'

urlpatterns = [
    path('', index, name='authsystem_index'),
]