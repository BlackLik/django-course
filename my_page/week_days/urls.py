from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('<str:name_day>/', views.DayView.as_view(), name='day'),
    path('day/<int:number_days>/', views.CounterDayView.as_view(), name='counter_day')
]