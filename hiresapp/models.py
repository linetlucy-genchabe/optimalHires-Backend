
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
import datetime as dt
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from djmoney.models.fields import MoneyField
from django.db.models.signals import post_save
from django.dispatch import receiver
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

JOBCATEGORY_CHOICES = (
    ("Technology", "Technology"),
    ("Business", "Business"),
    ("Engineering", "Engineering"),
    ("Agriculture", "Agriculture"),
    ("Freelance", "Freelance"),
    ("Part time", "Part time"),
    ("Full time", "Full time"),
    ("Contract", "Contract"),
)

class JobseekerProfile(models.Model):
    # user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='jobseekerprofile',default=None)
    jobseeker = models.OneToOneField(Jobseeker, on_delete = models.CASCADE, primary_key = True)
    about_me = models.TextField(max_length=1000, null=True,blank=True)
    phone_number = models.CharField(max_length=20)
    email= models.EmailField(max_length=254)
    location = models.CharField(max_length=20)
    educational_qualification = models.CharField(max_length=254,null=True,blank=True)
    professional_designation = models.CharField(max_length=254, null=True,blank=True)
    experience_years= models.CharField(max_length=20, null=True,blank=True)
    employer = models.ForeignKey(Employer, on_delete=models.SET_NULL, null=True,blank=True)
    job_category= models.CharField(max_length = 20, choices = JOBCATEGORY_CHOICES, default = 'Technology')
    salary = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    availability=models.CharField(max_length=70)
    create_at=models.DateTimeField(auto_now_add=True, null=True,blank=True)


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
    

    def __str__(self):
        return self.jobseeker.fullname
    
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
    

    def __str__(self):
        return self.jobseeker.fullname

class EmployerProfile(models.Model):
    employer = models.OneToOneField(Employer, on_delete = models.CASCADE, primary_key = True)
    current_opportunities = models.TextField(max_length=250, null=True, blank=True)
    employee_benefits=models.TextField(max_length=2500, null=True, blank=True)
    # jobseeker_viewer = models.ManyToManyField(JobseekerProfile)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
        
    def save_profile(self):
        self.save()
    def __str__(self):
        return self.employer.name

@receiver(post_save, sender=Jobseeker)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        JobseekerProfile.objects.create(user=instance)
    instance.jobseekerprofile.save()


@receiver(post_save, sender=Employer)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        EmployerProfile.objects.create(user=instance)
    instance.employerprofile.save()