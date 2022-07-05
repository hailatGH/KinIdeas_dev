from rest_framework import generics

from .models import Artist, Album, Genre, Track
from .serializers import ArtistSerializer, AlbumSerializer, TrackSerializer, GenreSerializer

# Create your views here.

class ArtistListCreateAPIView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

artist_list_create_view = ArtistListCreateAPIView.as_view()

class ArtistDetailAPIView(generics.RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

artist_detail_view = ArtistDetailAPIView.as_view()

class ArtistUpdateAPIView(generics.UpdateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

artist_update_view = ArtistUpdateAPIView.as_view()


class ArtistDestroyAPIView(generics.DestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

artist_destroy_view = ArtistDestroyAPIView.as_view()

class AlbumListCreateAPIView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

album_list_create_view = AlbumListCreateAPIView.as_view()

class AlbumDetailAPIView(generics.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

album_detail_view = AlbumDetailAPIView.as_view()

class AlbumUpdateAPIView(generics.UpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

album_update_view = AlbumUpdateAPIView.as_view()


class AlbumDestroyAPIView(generics.DestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

album_destroy_view = AlbumDestroyAPIView.as_view()

class TrackListCreateAPIView(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

track_list_create_view = TrackListCreateAPIView.as_view()

class TrackDetailAPIView(generics.RetrieveAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

track_detail_view = TrackDetailAPIView.as_view()

class TrackUpdateAPIView(generics.UpdateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

track_update_view = TrackUpdateAPIView.as_view()


class TrackDestroyAPIView(generics.DestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

track_destroy_view = TrackDestroyAPIView.as_view()

class GenreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

genre_list_create_view = GenreListCreateAPIView.as_view()

class GenreDetailAPIView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

genre_detail_view = GenreDetailAPIView.as_view()

class GenreUpdateAPIView(generics.UpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

genre_update_view = GenreUpdateAPIView.as_view()

class GenreDestroyAPIView(generics.DestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

genre_destroy_view = GenreDestroyAPIView.as_view()