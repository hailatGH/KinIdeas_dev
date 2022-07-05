from rest_framework import generics

from .models import Radio
from .serializers import RadioSerializer
# Create your views here.

class RadioListCreateAPIView(generics.ListCreateAPIView):
    queryset = Radio.objects.all()
    serializer_class = RadioSerializer

radio_list_create_view = RadioListCreateAPIView.as_view()

class RadioDetailAPIView(generics.RetrieveAPIView):
    queryset = Radio.objects.all()
    serializer_class = RadioSerializer

radio_detail_view = RadioDetailAPIView.as_view()

class RadioUpdateAPIView(generics.UpdateAPIView):
    queryset = Radio.objects.all()
    serializer_class = RadioSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

radio_update_view = RadioUpdateAPIView.as_view()


class RadioDestroyAPIView(generics.DestroyAPIView):
    queryset = Radio.objects.all()
    serializer_class = RadioSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

radio_destroy_view = RadioDestroyAPIView.as_view()