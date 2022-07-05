from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Season, Host, Episode, Category

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = [
            'id',
            'episode_name',
            'episode_description',
            'episode_category',
            'season',
            'episode_file',
        ]

class CategorySerializer(serializers.ModelSerializer):
    episode = EpisodeSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = [
            'id',
            'category_name',
            'category_description',
            'episode',
        ]

class SeasonSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, required=False)

    class Meta:
        model = Season
        fields = [
            'id',
            'season_name',
            'season_cover',
            'season_description',
            'season_release_date',
            'host',
            'episodes',
        ]

class HostSerializer(serializers.ModelSerializer):
    seasons = SeasonSerializer(many=True, required=False)
    
    class Meta:
        model = Host
        fields = [
            'id',
            'host_name',
            'host_avatar',
            'host_description',
            'seasons',
        ]