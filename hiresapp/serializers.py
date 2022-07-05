from rest_framework import serializers
from .models import *
from dataclasses import fields
from django.forms import CharField
# from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'password']


        
class JobseekerSignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model=User
        fields=['username', 'email','password', 'password2']
        
        extra_kwargs={
            'password':{'write_only':'True'}
        }
        
        
    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],   
        )
        password=self.validated_data['password']
        password2=self.validated_data['password']
        
        if password != password2:
            raise serializers.ValidationError({'error':'check your passwords'})
        user.set_password(password)
        user.is_jobseeker=True
        user.save()
        Jobseeker.objects.create(user=user)
        return user
            
class EmployerSignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model=User
        fields=['username', 'email','password', 'password2']
        
        extra_kwargs={
            'password':{'write_only':'True'}
        }
        
        
    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],   
        )
        password=self.validated_data['password']
        password2=self.validated_data['password']
        
        if password != password2:
            raise serializers.ValidationError({'error':'check your passwords'})
        user.set_password(password)
        user.is_employer=True
        user.save()
        Employer.objects.create(user=user)
        return user
            

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("pk", 'user','firstname','lastname','email','profile_pic','bio') 


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ('jobId','title', 'description', 'location', 'job_type', 'job_category','last_date', 'company_name', 'company_description', 'website','created_at',)

        
class JobseekerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jobseeker
        fields = ('jobseekerId','fullname', 'image', 'gender','resume',)


        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('CategoryId','name')

        
class EmployerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employer
        fields = ('employerId','name', 'contact','description',)