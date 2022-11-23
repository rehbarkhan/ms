from django import forms
from dean.models import DeanDepartment


class DeanDepartmentForm(forms.ModelForm):

    class Meta:

        model = DeanDepartment

        exclude = ('user','salary','account_type')

        widgets = {
            'firstname':forms.TextInput(attrs={'placeholder':
            'First Name','class':'form-control'}),
            'middlename':forms.TextInput(attrs={'placeholder':
            'Middle Name','class':'form-control'}),
            'lastname':forms.TextInput(attrs={'placeholder':
            'Last Name','class':'form-control'}),
            'date_of_birth':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'mobile':forms.TextInput(attrs={'placeholder':
            'Mobile Number','class':'form-control'}),
            'emergency_mobile':forms.TextInput(attrs={'placeholder':
            'Emergency Mobile Number','class':'form-control'}),
            'present_address':forms.TextInput(attrs={'placeholder':
            'Present Address','class':'form-control'}),
            'present_city':forms.TextInput(attrs={'placeholder':
            'Present City','class':'form-control'}),
            'present_state':forms.TextInput(attrs={'placeholder':
            'Present State','class':'form-control'}),
            'present_zip':forms.TextInput(attrs={'placeholder':
            'Present Zip Code','class':'form-control'}),
            'permanent_address':forms.TextInput(attrs={'placeholder':
            'Permanent Address','class':'form-control'}),
            'permanent_city':forms.TextInput(attrs={'placeholder':
            'Permanent City','class':'form-control'}),
            'permanent_state':forms.TextInput(attrs={'placeholder':
            'Permanent State','class':'form-control'}),
            'permanent_zip':forms.TextInput(attrs={'placeholder':
            'Permanent Zip Code','class':'form-control'}),
            'package_lpa':forms.TextInput(attrs={'placeholder':
            'CTC LPA','class':'form-control'}),
        }
