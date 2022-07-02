from django.urls import re_path as url, include

from hiresapp.models import Jobseeker
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



urlpatterns = [
    # url(r'^$', views.index, name= 'index'),

    url(r'^api/$', views.JobseekerViewset.as_view({'get': 'list'})),
    url(r'^api/$', views.EmployerViewset.as_view({'get': 'list'})),
    url(r'^api/$', views.JobViewset.as_view({'get': 'list'})),
    url(r'^api/$', views.JobtypeViewset.as_view({'get': 'list'})),
    url(r'^api/$', views.CategoryViewset.as_view({'get': 'list'})),
   
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


urlpatterns +=routes.urls