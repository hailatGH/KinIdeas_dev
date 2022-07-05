from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Album, Artist, Track, Genre

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = [
            'id',
            'track_name',
            'track_description',
            'track_genre',
            'album',
            'track_file',
        ]

class GenreSerializer(serializers.ModelSerializer):
    track = TrackSerializer(many=True, required=False)

    class Meta:
        model = Genre
        fields = [
            'id',
            'genre_name',
            'genre_description',
            'track',
        ]

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, required=False)

    class Meta:
        model = Album
        fields = [
            'id',
            'album_name',
            'album_description',
            'album_release_date',
            'album_cover',
            'artist',
            'tracks',
        ]

class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, required=False)
    
    class Meta:
        model = Artist
        fields = [
            'id',
            'artist_name',
            'artist_avatar',
            'artist_description',
            'albums',
        ]