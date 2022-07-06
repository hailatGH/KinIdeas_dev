from rest_framework import generics

from .models import CompanyProfile
from .serializers import CompanyProfileSerializer
# Create your views here.

class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer

profile_list_create_view = ProfileListCreateAPIView.as_view()

class ProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer

profile_detail_view = ProfileDetailAPIView.as_view()

class ProfileUpdateAPIView(generics.UpdateAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

profile_update_view = ProfileUpdateAPIView.as_view()


class ProfileDestroyAPIView(generics.DestroyAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

profile_destroy_view = ProfileDestroyAPIView.as_view()