from django.urls import re_path as url, include

from hiresapp.models import *
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

routes = DefaultRouter()
routes.register('jobseeker', views.JobseekerViewset, basename='jobseeker')
routes.register('job', views.JobViewset, basename='job')
routes.register('employer', views.EmployerViewset, basename='employer')
routes.register('jobtype', views.JobtypeViewset, basename='jobtype')
routes.register('category', views.CategoryViewset, basename='category')
routes.register('jobseekerprofile', views.JobseekerProfileViewset, basename='jobseekerprofile')
routes.register('employerprofile', views.EmployerProfileViewset, basename='employerprofile')



urlpatterns = [
    # url(r'^$', views.index, name= 'index'),

    url(r'^api/jobseeker$', views.JobseekerViewset.as_view({'get': 'list'})),
    url(r'^api/employer$', views.EmployerViewset.as_view({'get': 'list'})),
    url(r'^api/job$', views.JobViewset.as_view({'get': 'list'})),
    url(r'^api/jobtype$', views.JobtypeViewset.as_view({'get': 'list'})),
    url(r'^api/category$', views.CategoryViewset.as_view({'get': 'list'})),
    url(r'^api/jobseekerprofile$', views.JobseekerProfileViewset.as_view({'get': 'list'})),
    url(r'^api/employerprofile$', views.EmployerProfileViewset.as_view({'get': 'list'})),
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


urlpatterns +=routes.urls