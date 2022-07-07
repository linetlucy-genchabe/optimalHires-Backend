from django import forms
from django.contrib.auth.models import User
from users.models import JobseekerProfile, EmployerProfile
# from django import forms
# from django.utils import six
# from djng.forms import fields, NgDeclarativeFieldsMetaclass, NgModelFormMixin


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