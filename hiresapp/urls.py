from django.urls import re_path as url, include, path

from hiresapp.models import *
from . import views
from .views import *
from django.conf import settings

from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

routes = DefaultRouter()
routes.register('jobseeker', views.JobseekerViewset, basename='jobseeker')
routes.register('job', views.JobViewset, basename='job')
routes.register('employer', views.EmployerViewset, basename='employer')

routes.register('category', views.CategoryViewset, basename='category')



urlpatterns = [
    # url(r'^$', views.index, name= 'index'),

    url(r'^api/jobseeker$', views.JobseekerViewset.as_view({'get': 'list'})),
    url(r'^api/employer$', views.EmployerViewset.as_view({'get': 'list'})),
    url(r'^api/job$', views.JobViewset.as_view({'get': 'list'})),
    
    url(r'^api/category$', views.CategoryViewset.as_view({'get': 'list'})),

    path('signup/jobseeker/', views.JobseekerSignUpView.as_view()),
    path('signup/employer/', views.EmployerSignUpView.as_view()),
    path('login/', views.CustomAuthToken.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('jobseeker/dashboard/',views. JobseekerOnlyView.as_view(), name='jobseekers'),
    path('employer/dashboard/', views.EmployerOnlyView.as_view(), name='employers')
   
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


urlpatterns +=routes.urls