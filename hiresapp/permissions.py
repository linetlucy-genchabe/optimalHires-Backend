from rest_framework.permissions import BasePermission



class IsJobseekerUser(BasePermission):
    def has_permission(self,request,view):
        return bool(request.user and request.user.is_jobseeker)
    
class IsEmployerUser(BasePermission):
    def has_permission(self,request,view):
        return bool(request.user and request.user.is_employer)