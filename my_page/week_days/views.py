from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
name_days = {
    "monday": "",
    "tuesday": "",
    "wednesday": "",
    "thursday": "",
    "friday": "",
    "saturday": "",
    "sunday": ""
}


class HomeView(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the home page.")


class DayView(View):
    def get(self, request, name_day):
        global name_days

        if name_day not in name_days.keys():
            return HttpResponseNotFound("Not found")
        return HttpResponse(f"Hello, world. You're at the {name_day} page.")


class CounterDayView(View):
    def get(self, request, number_days: int):
        global name_days

        all_days = list(name_days.keys())

        if number_days not in range(len(all_days)):
            return HttpResponseNotFound("Not found")
        # return HttpResponse(f'Сегодня {number_days} день недели')
        return HttpResponseRedirect(f'../{all_days[number_days]}')
