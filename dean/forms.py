from django import forms
from dean.models import DeanDepartment


class DeanDepartmentForm(forms.ModelForm):

    class Meta:

        model = DeanDepartment

        exclude = ('user','salary','account_type')

        widgets = {
            'firstname':forms.TextInput(attrs={'placeholder':
            'First Name','class':'form-control mb-2'}),
            'middlename':forms.TextInput(attrs={'placeholder':
            'Middle Name','class':'form-control mb-2'}),
            'lastname':forms.TextInput(attrs={'placeholder':
            'Last Name','class':'form-control mb-5'}),
            'date_of_birth':forms.DateInput(attrs={'type':'date','class':'form-control mb-5'}),
            'mobile':forms.TextInput(attrs={'placeholder':
            'Mobile Number','class':'form-control mb-2'}),
            'emergency_mobile':forms.TextInput(attrs={'placeholder':
            'Emergency Mobile Number','class':'form-control mb-5'}),
            'present_address':forms.TextInput(attrs={'placeholder':
            'Present Address','class':'form-control mb-2'}),
            'present_city':forms.TextInput(attrs={'placeholder':
            'Present City','class':'form-control mb-2'}),
            'present_state':forms.TextInput(attrs={'placeholder':
            'Present State','class':'form-control mb-2'}),
            'present_zip':forms.TextInput(attrs={'placeholder':
            'Present Zip Code','class':'form-control mb-5'}),
            'permanent_address':forms.TextInput(attrs={'placeholder':
            'Permanent Address','class':'form-control mb-2'}),
            'permanent_city':forms.TextInput(attrs={'placeholder':
            'Permanent City','class':'form-control mb-2'}),
            'permanent_state':forms.TextInput(attrs={'placeholder':
            'Permanent State','class':'form-control mb-2'}),
            'permanent_zip':forms.TextInput(attrs={'placeholder':
            'Permanent Zip Code','class':'form-control mb-5'}),
            'package_lpa':forms.TextInput(attrs={'placeholder':
            'CTC LPA','class':'form-control mb-5'}),
        }
