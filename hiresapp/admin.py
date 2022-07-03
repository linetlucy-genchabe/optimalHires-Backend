from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Jobseeker)
admin.site.register(Category)
admin.site.register(Employer)
admin.site.register(Jobtype)
admin.site.register(Job)
admin.site.register(JobseekerProfile)
admin.site.register(EmployerProfile)
