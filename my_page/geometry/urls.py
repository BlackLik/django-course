from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle_area, name='rectangle'),
    path('circle/<int:radius>/', views.get_circle_area, name='circle'),
    path('square/<int:width>/', views.get_square_area, name='square'),
    path('get_rectangle_area/<int:width>/<int:height>/', views.redirect_to_rectangle_area, name='redirect_to_rectangle_area,'),
    path('get_square_area/<int:width>/', views.redirect_to_square_area, name='redirect_to_square_area'),
    path('get_circle_area/<int:radius>/', views.redirect_to_circle_area, name='redirect_to_circle_area')
]