from django.urls import re_path as url, include, path


from hiresapp.models import *
from . import views
from .views import *
from django.conf import settings

from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Optimal-Hires",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


routes = DefaultRouter()
routes.register('jobseeker', views.JobseekerViewset, basename='jobseeker')
routes.register('job', views.JobViewset, basename='job')
routes.register('employer', views.EmployerViewset, basename='employer')

routes.register('category', views.CategoryViewset, basename='category')
routes.register('jobseekerprofile', views.JobseekerProfileViewset, basename='jobseekerprofile')
# routes.register('employerprofile', views.EmployerProfileViewset, basename='employerprofile')



urlpatterns = [
    # url(r'^$', views.index, name= 'index'),
    url(r'^api/jobseeker$', views.JobseekerViewset.as_view({'get': 'list'})),
    url(r'^api/employer$', views.EmployerViewset.as_view({'get': 'list'})),
    url(r'^api/job$', views.JobViewset.as_view({'get': 'list'})),
    
    url(r'^api/category$', views.CategoryViewset.as_view({'get': 'list'})),
    url(r'^api/jobseekerprofile$', views.JobseekerProfileViewset.as_view({'get': 'list'})),
    # url(r'^api/employerprofile$', views.EmployerProfileViewset.as_view({'get': 'list'})),
    # url(r'^upload/$', FileUploadView.as_view(), name='fileupload'),
    

    path('signup/jobseeker/', views.JobseekerSignUpView.as_view()),
    path('signup/employer/', views.EmployerSignUpView.as_view()),
    path('login/', views.CustomAuthToken.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('jobseeker/dashboard/',views. JobseekerOnlyView.as_view(), name='jobseekers'),
    path('employer/dashboard/', views.EmployerOnlyView.as_view(), name='employers'),

    # url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
   
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


urlpatterns +=routes.urls