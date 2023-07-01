from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('<int:id_post>/', views.PostDetailView.as_view(), name='post-detail'),
    path('<str:name_post>/', views.PostView.as_view(), name='post'),
]