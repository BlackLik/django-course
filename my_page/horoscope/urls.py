from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:index_zodiac>/', views.index_zodiac, name='index_zodiac'),
    path('<str:zodiac>/', views.zodiac, name='zodiac'),
    
]
