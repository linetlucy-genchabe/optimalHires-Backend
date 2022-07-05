
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
import datetime as dt
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

# Create your models here.



class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_employer = models.BooleanField('Is employer', default=False)
    is_jobseeker = models.BooleanField('Is jobseeker', default=False)
    
    def __str__(self):
        return self.username

    #using signals 
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        

class Admin(models.Model):
    user=models.OneToOneField(User ,related_name='admin',on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.username
    
  
class Category(models.Model):
    CategoryId = models.AutoField(primary_key=True,default=None)
    name = models.CharField(max_length=50, unique=True)
    
    
    def __str__(self):
        return self.name


    def save_category(self):
        self.save()

class Jobseeker(models.Model):
    user=models.OneToOneField(User ,related_name='jobseeker',on_delete=models.CASCADE,default=None)
    jobseekerId = models.AutoField(primary_key=True,default=None)
    fullname = models.CharField(max_length=60)
    image = CloudinaryField('pic')
    gender = models.CharField(max_length=10)
    resume = CloudinaryField('resume')
 
    # def __str__(self):
    #     return self.fullname

class Employer(models.Model):
    user=models.OneToOneField(User ,related_name='employer',on_delete=models.CASCADE, default=None)
    employerId = models.AutoField(primary_key=True,default=None)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    
 
    # def __str__ (self):
    #     return self.user.username

class Job(models.Model):
    jobId = models.AutoField(primary_key=True, default=None)
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=150)
    job_type = models.CharField(max_length=50)
    job_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    last_date = models.DateTimeField()
    company_name = models.CharField(max_length=100)
    company_description = models.CharField(max_length=1000)
    website = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save_job(self):
        self.save()

    def delete_job(self):
        self.delete()
        
        
    def update_job(self):
        self.update_job()

    def __str__(self):
        return self.title

    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    firstname=models.CharField(max_length=100,blank=True,null=True)
    lastname=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    profile_pic=models.ImageField(upload_to='images_uploaded', null=True)
    bio=models.TextField(blank=True,null=True)
    
    #Signals for saving profile when a user is created
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
        
    def save_profile(self):
        self.save()
    

