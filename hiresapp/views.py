from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework import status, viewsets,permissions,generics
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from .permissions import IsJobseekerUser,IsEmployerUser
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken 

# from drf_yasg.utils import swagger_auto_schema
from rest_framework.schemas import get_schema_view

# Create your views here.


def index(request):
   
    
    return render(request, 'index.html')

# #Application views.
# class UpdateProfile(APIView):
#     serializer_class = ProfileSerializer
#     lookup_field = 'email'
#     profiles = Profile.objects.all()
  
#     def put(self, request, *args, **kwargs):
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobseekerViewset(viewsets.ModelViewSet):
    serializer_class = JobseekerSerializer
    queryset = Jobseeker.objects.all()



class EmployerViewset(viewsets.ModelViewSet):
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()


class JobViewset(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()


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


#views
# @swagger_auto_schema(request_body=JobseekerSignUpSerializer)
class JobseekerSignUpView(generics.GenericAPIView):
    serializer_class=JobseekerSignUpSerializer
    def post(self, request, *args, **kwargs):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "Token":Token.objects.get(user=user).key,
            "message":"jobseeker Registration successful.You are now registered as a staff"
        })

class EmployerSignUpView(generics.GenericAPIView):
    serializer_class=EmployerSignUpSerializer
    def post(self, request, *args, **kwargs):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "Token":Token.objects.get(user=user).key,
            "message":"Employer Registration successful.You are now registered as an Employer"
        })
        
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created=Token.objects.get_or_create(user=user)
        
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'is_jobseeker':user.is_jobseeker,
            'is_employer':user.is_employer
        })
        
class LogoutView(APIView):
    def post(self,request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)
    
class JobseekerOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsJobseekerUser]
    serializer_class=UserSerializer
    
    def get_object(self):
        return self.request.user
    
class EmployerOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsEmployerUser]
    serializer_class=UserSerializer
    
    def get_object(self):
        return self.request.user
