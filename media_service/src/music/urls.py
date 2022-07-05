from django.urls import path

from . import views

urlpatterns = [
    path('artist/', views.artist_list_create_view),
    path('artist/<int:pk>/update/', views.artist_update_view),
    path('artist/<int:pk>/delete/', views.artist_destroy_view),
    path('artist/<int:pk>/', views.artist_detail_view),

    path('album/', views.album_list_create_view),
    path('album/<int:pk>/update/', views.album_update_view),
    path('album/<int:pk>/delete/', views.album_destroy_view),
    path('album/<int:pk>/', views.album_detail_view),

    path('track/', views.track_list_create_view),
    path('track/<int:pk>/update/', views.track_update_view),
    path('track/<int:pk>/delete/', views.track_destroy_view),
    path('track/<int:pk>/', views.track_detail_view),

    path('genre/', views.genre_list_create_view),
    path('genre/<int:pk>/update/', views.genre_update_view),
    path('genre/<int:pk>/delete/', views.genre_destroy_view),
    path('genre/<int:pk>/', views.genre_detail_view)
]