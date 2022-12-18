from django import forms
from student.models import Course,Student


# Course Form
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Course Name','class':'form-control'}),
            'description':forms.TextInput(attrs={'placeholder':'Course Description','class':'form-control'}),
            'duration':forms.TextInput(attrs={'placeholder':'Course Duration','class':'form-control'}),
            'fee':forms.TextInput(attrs={'placeholder':'Course Fee','class':'form-control'})
        }

# Student Form
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields ='__all__'
        exclude = ('user',)
        widgets = {
            'firstname':forms.TextInput(attrs={'placeholder':
            'First Name','class':'form-control mb-2'}),
            'middlename':forms.TextInput(attrs={'placeholder':
            'Middle Name','class':'form-control mb-2'}),
            'lastname':forms.TextInput(attrs={'placeholder':
            'Last Name','class':'form-control mb-5'}),
            'date_of_birth':forms.DateInput(attrs={'type':'date','class':'form-control mb-5','placeholder':'Date of Birth','onfocus':"(this.type='date')",'onblur':"(this.type='text')"}),
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
            'actual_fee':forms.NumberInput(attrs={'placholder':'Actual Fee','class':'form-control mb-5'})
        }