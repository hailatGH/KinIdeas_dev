from rest_framework import generics

from .models import Host, Season, PodcastCategory, Episode
from .serializers import HostSerializer, SeasonSerializer, EpisodeSerializer, PodcastCategorySerializer

# Create your views here.

class HostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

host_list_create_view = HostListCreateAPIView.as_view()

class HostDetailAPIView(generics.RetrieveAPIView):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

host_detail_view = HostDetailAPIView.as_view()

class HostUpdateAPIView(generics.UpdateAPIView):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

host_update_view = HostUpdateAPIView.as_view()


class HostDestroyAPIView(generics.DestroyAPIView):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

host_destroy_view = HostDestroyAPIView.as_view()

class SeasonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

season_list_create_view = SeasonListCreateAPIView.as_view()

class SeasonDetailAPIView(generics.RetrieveAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

season_detail_view = SeasonDetailAPIView.as_view()

class SeasonUpdateAPIView(generics.UpdateAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

season_update_view = SeasonUpdateAPIView.as_view()


class SeasonDestroyAPIView(generics.DestroyAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

season_destroy_view = SeasonDestroyAPIView.as_view()

class EpisodeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

episode_list_create_view = EpisodeListCreateAPIView.as_view()

class EpisodeDetailAPIView(generics.RetrieveAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

episode_detail_view = EpisodeDetailAPIView.as_view()

class EpisodeUpdateAPIView(generics.UpdateAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

episode_update_view = EpisodeUpdateAPIView.as_view()


class EpisodeDestroyAPIView(generics.DestroyAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

episode_destroy_view = EpisodeDestroyAPIView.as_view()

class PodcastCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = PodcastCategory.objects.all()
    serializer_class = PodcastCategorySerializer

podcast_category_list_create_view = PodcastCategoryListCreateAPIView.as_view()

class PodcastCategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = PodcastCategory.objects.all()
    serializer_class = PodcastCategorySerializer

podcast_category_detail_view = PodcastCategoryDetailAPIView.as_view()

class PodcastCategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = PodcastCategory.objects.all()
    serializer_class = PodcastCategorySerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

podcast_category_update_view = PodcastCategoryUpdateAPIView.as_view()

class PodcastCategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = PodcastCategory.objects.all()
    serializer_class = PodcastCategorySerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

podcast_category_destroy_view = PodcastCategoryDestroyAPIView.as_view()