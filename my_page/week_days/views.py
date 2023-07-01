from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


class HomeView(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the home page.")


class DayView(View):
    def get(self, request, name_day):
        name_days = [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday"
        ]
        
        if name_day not in name_days:
            return HttpResponseNotFound("Not found")
        return HttpResponse(f"Hello, world. You're at the {name_day} page.")

class CounterDayView(View):
    def get(self, request, number_days: int):
        if number_days < 0 or number_days > 7:
            return HttpResponseNotFound("Not found")
        return HttpResponse(f'Сегодня {number_days} день недели')