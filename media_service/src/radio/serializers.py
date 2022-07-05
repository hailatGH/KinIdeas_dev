from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Radio

class RadioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Radio
        fields = [
            'id',
            'station_name',
            'station_frequency',
            'station_url',
            'station_description',
            'cover_image',
        ]