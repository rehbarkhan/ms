from django.urls import path
from dean.views import (
    Index,AdmissionApproval,AdmissinApprovalLink,
    CourseDetails,FinanceApprove,FinanceApproval,
    EditCourse,DeanNewStaff
)
app_name = 'dean'

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('admission/',AdmissionApproval.as_view(),name='admission'),
    path('admissionapr/<str:u_name>/',AdmissinApprovalLink.as_view(),name='admission_apr_link'),
    path('courses/',CourseDetails.as_view(),name='course'),
    path('finance/',FinanceApprove.as_view(),name='financestaff'),
    path('financeapr/<int:pk>/',FinanceApproval.as_view(),name='financeapproval'),
    path('editcourse/<int:pk>/',EditCourse.as_view(),name='edit-course'),
    path('newstaff/',DeanNewStaff.as_view(),name='staff')
]