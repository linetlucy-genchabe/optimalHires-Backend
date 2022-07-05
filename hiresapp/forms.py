from django import forms
from django.contrib.auth.models import User
# from .models import Applicant,Company
from users.models import JobseekerProfile, EmployerProfile


class JobseekerProfileForm(forms.ModelForm):
    image = CloudinaryField('pic')
    class Meta:
        model =  JobseekerProfile
        exclude = ['user', 'applicantId']       


class EmployerProfileForm(forms.ModelForm):
    image = CloudinaryField('image')
    class Meta:
        model = EmployerProfile
        exclude = ['user', 'companyId']                 