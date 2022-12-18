from django.urls import path
from admission.views import Index,Account,Profile,StudentProfile,Finance,AdmissionProfilePasswordReset
app_name = 'admission'
urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('account/',Account.as_view(),name='account'),
    path('profile/',Profile.as_view(),name='profile'),
    path('student/',StudentProfile.as_view(),name='student-profile'),
    path('finance/',Finance.as_view(),name='finance'),
    path('passreset/',AdmissionProfilePasswordReset.as_view(),name='profile-reset')
]
