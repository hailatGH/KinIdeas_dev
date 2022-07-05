from django.urls import path

from . import views

urlpatterns = [
    path('host/', views.host_list_create_view),
    path('host/<int:pk>/update/', views.host_update_view),
    path('host/<int:pk>/delete/', views.host_destroy_view),
    path('host/<int:pk>/', views.host_detail_view),

    path('season/', views.season_list_create_view),
    path('season/<int:pk>/update/', views.season_update_view),
    path('season/<int:pk>/delete/', views.season_destroy_view),
    path('season/<int:pk>/', views.season_detail_view),

    path('episode/', views.episode_list_create_view),
    path('episode/<int:pk>/update/', views.episode_update_view),
    path('episode/<int:pk>/delete/', views.episode_destroy_view),
    path('episode/<int:pk>/', views.episode_detail_view),

    path('category/', views.category_list_create_view),
    path('category/<int:pk>/update/', views.category_update_view),
    path('category/<int:pk>/delete/', views.category_destroy_view),
    path('category/<int:pk>/', views.category_detail_view)
]