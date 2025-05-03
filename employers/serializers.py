from rest_framework import serializers
from .models import Employer

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at')

    def validate_email(self, value):
        # Add custom email validation if needed
        return value

    def validate_phone_number(self, value):
        # Add custom phone validation if needed
        return value
    
from rest_framework import permissions

class IsEmployerOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user