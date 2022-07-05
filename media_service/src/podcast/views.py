from rest_framework import generics

from .models import Host, Season, Category, Episode
from .serializers import HostSerializer, SeasonSerializer, EpisodeSerializer, CategorySerializer

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

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

category_list_create_view = CategoryListCreateAPIView.as_view()

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

category_detail_view = CategoryDetailAPIView.as_view()

class CategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

category_update_view = CategoryUpdateAPIView.as_view()

class CategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

category_destroy_view = CategoryDestroyAPIView.as_view()