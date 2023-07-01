from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle_area, name='rectangle'),
    path('circle/<int:radius>/', views.get_circle_area, name='circle'),
    path('square/<int:width>/', views.get_square_area, name='square')
]