from django.urls import path

from . import views

urlpatterns = [
    path('profile/', views.profile_list_create_view),
    path('profile/<int:pk>/update/', views.profile_update_view),
    path('profile/<int:pk>/delete/', views.profile_destroy_view),
    path('profile/<int:pk>/', views.profile_detail_view),
]