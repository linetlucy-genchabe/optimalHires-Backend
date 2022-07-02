from django.urls import re_path as url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    # url(r'^job/$', views.JobApi),
    # url(r'^company/$', views.CompanyList.as_view),
    url(r'^api/jobseeker/$', views.JobseekerViewset.as_view({'get': 'list'})),
    url(r'^api/employer/$', views.EmployerViewset.as_view({'get': 'list'})),
    url(r'^api/job/$', views.JobViewset.as_view({'get': 'list'})),
    url(r'^api/jobtype/$', views.JobtypeViewset.as_view({'get': 'list'})),
    url(r'^api/categories/$', views.CategoryViewset.as_view({'get': 'list'})),
    
    # url(r'register/$',views.register ),
    # url(r'accounts/login/$',views.user_login, name='login'),
    # url(r'logout/$',views.signout),
    # url(r'^accounts/profile/$', views.user_profiles, name='profile'),

   
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)