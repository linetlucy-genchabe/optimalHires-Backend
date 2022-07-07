from rest_framework import serializers
from .models import *
# from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'id',

        ]

class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ('jobId','title', 'description', 'location', 'job_type', 'job_category','last_date', 'company_name', 'company_description', 'website','created_at',)

        
class JobseekerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jobseeker
        fields = ('jobseekerId','fullname', 'image', 'gender','resume',)


        
class JobtypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jobtype
        fields = ('jobtypeId','name')


        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('CategoryId','name')

        
class EmployerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employer
        fields = ('employerId','name', 'contact', 'image','description',)

class JobseekerProfileSerializer(serializers.HyperlinkedModelSerializer):
    jobseeker = JobseekerSerializer()
    # employer = EmployerSerializer()
    class Meta:
        model = JobseekerProfile
        fields = ('jobseeker','about_me','phone_number', 'email', 'location','educational_qualification','professional_designation', 'experience_years','employer','job_category','salary','create_at',)

class EmployerProfileSerializer(serializers.HyperlinkedModelSerializer):
    employer = EmployerSerializer()
    # jobseeker_viewer = JobseekerProfileSerializer()
    class Meta:
        model = EmployerProfile
        fields = ('employer','current_opportunities','employee_benefits',)

class JobseekerProfileSerializer(serializers.HyperlinkedModelSerializer):
    jobseeker = JobseekerSerializer()
    # employer = EmployerSerializer()
    class Meta:
        model = JobseekerProfile
        fields = ('jobseeker','about_me','phone_number', 'email', 'location','educational_qualification','professional_designation', 'experience_years','employer','job_category','salary','create_at',)
