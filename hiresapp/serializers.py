from rest_framework import serializers
from .models import *


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('jobId','title', 'description', 'location', 'job_type', 'job_category','last_date', 'company_name', 'company_description', 'website','created_at',)

        
class JobseekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobseeker
        fields = ('jobseekerId','fullname', 'image', 'gender','resume',)


        
class JobtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobtype
        fields = ('jobtypeId','name')


        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('CategoryId','name')

        
class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ('employerId','name', 'contact', 'image','description',)