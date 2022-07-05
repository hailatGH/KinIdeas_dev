from django.urls import path

from . import views

urlpatterns = [
    path('', views.radio_list_create_view),
    path('<int:pk>/update/', views.radio_update_view),
    path('<int:pk>/delete/', views.radio_destroy_view),
    path('<int:pk>/', views.radio_detail_view),
]