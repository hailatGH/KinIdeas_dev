from django.urls import path

from . import views

urlpatterns = [
    path('', views.profile_list_create_view),
    path('<int:pk>/update/', views.profile_update_view),
    path('<int:pk>/delete/', views.profile_destroy_view),
    path('<int:pk>/', views.profile_detail_view),
]