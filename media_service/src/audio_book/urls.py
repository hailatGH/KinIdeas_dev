from django.urls import path

from . import views

urlpatterns = [
    path('writer/', views.writer_list_create_view),
    path('writer/<int:pk>/update/', views.writer_update_view),
    path('writer/<int:pk>/delete/', views.writer_destroy_view),
    path('writer/<int:pk>/', views.writer_detail_view),

    path('narrator/', views.narrator_list_create_view),
    path('narrator/<int:pk>/update/', views.narrator_update_view),
    path('narrator/<int:pk>/delete/', views.narrator_destroy_view),
    path('narrator/<int:pk>/', views.narrator_detail_view),

    path('category/', views.category_list_create_view),
    path('category/<int:pk>/update/', views.category_update_view),
    path('category/<int:pk>/delete/', views.category_destroy_view),
    path('category/<int:pk>/', views.category_detail_view),

    path('book/', views.book_list_create_view),
    path('book/<int:pk>/update/', views.book_update_view),
    path('book/<int:pk>/delete/', views.book_destroy_view),
    path('book/<int:pk>/', views.book_detail_view),

    path('chapter/', views.chapter_list_create_view),
    path('chapter/<int:pk>/update/', views.chapter_update_view),
    path('chapter/<int:pk>/delete/', views.chapter_destroy_view),
    path('chapter/<int:pk>/', views.chapter_detail_view)
]