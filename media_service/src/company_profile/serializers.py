from rest_framework import serializers, status
from rest_framework.response import Response

from .models import CompanyProfile

class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = '__all__'