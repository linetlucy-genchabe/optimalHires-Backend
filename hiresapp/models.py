from django.db import models

# Create your models here.
from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404

# Create your models here.
class Jobtype(models.Model):
    jobtypeId = models.AutoField(primary_key=True,default=None)
    name= models.CharField(max_length=100)

  
class Category(models.Model):
    CategoryId = models.AutoField(primary_key=True,default=None)
    name = models.CharField(max_length=50, unique=True)
    
    
    def __str__(self):
        return self.name


    def save_category(self):
        self.save()

class Jobseeker(models.Model):
    jobseekerId = models.AutoField(primary_key=True,default=None)
    fullname = models.CharField(max_length=60)
    image = CloudinaryField('pic')
    gender = models.CharField(max_length=10)
    resume = CloudinaryField('resume')
 
    def __str__(self):
        return self.fullname

class Employer(models.Model):
    employerId = models.AutoField(primary_key=True,default=None)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    image = CloudinaryField('image')
    description = models.CharField(max_length=1000)
    
 
    def __str__ (self):
        return self.name

class Job(models.Model):
    jobId = models.AutoField(primary_key=True, default=None)
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=150)
    job_type = models.ForeignKey(Jobtype, on_delete=models.CASCADE)
    job_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    last_date = models.DateTimeField()
    company_name = models.CharField(max_length=100)
    company_description = models.CharField(max_length=1000)
    website = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title



