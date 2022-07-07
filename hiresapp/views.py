from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework import generics
from rest_framework import status, viewsets
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

# Create your views here.


def index(request):
   
    
    return render(request, 'index.html')


class JobseekerViewset(viewsets.ModelViewSet):
    serializer_class = JobseekerSerializer
    queryset = Jobseeker.objects.all()



class EmployerViewset(viewsets.ModelViewSet):
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()


class JobViewset(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()


class JobtypeViewset(viewsets.ModelViewSet):
    serializer_class = JobtypeSerializer
    queryset = Jobtype.objects.all()


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    
class JobseekerProfileViewset(viewsets.ModelViewSet):
    serializer_class = JobseekerProfileSerializer
    queryset = JobseekerProfile.objects.all()

class  EmployerProfileViewset(viewsets.ModelViewSet):
    serializer_class =  EmployerProfileSerializer
    queryset =  EmployerProfile.objects.all()



# class JobseekerProfileFormView(FormView):
#     template = 'jobseekerprofile.component.html'
#     form_class = JobseekerProfileForm
#     success_url = reverse_lazy('success-page')

#     def post(self, request, **kwargs):
#         assert request.is_ajax()
#         request_data = json.loads(request.body)
#         form = self.form_class(data=request_data[self.form_class.scope_prefix])
#         if form.is_valid():
#             return JsonResponse({'success_url': force_text(self.success_url)})
#         else:
#             response_data = {form.form_name: form.errors}
#             return JsonResponse(response_data, status=422)