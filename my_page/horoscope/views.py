from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def zodiac(request, zodiac: str):
    all_zodiac = ['aries', 
                  'taurus', 
                  'gemini', 
                  'cancer', 
                  'leo',
                  'virgo',
                  'libra',  
                  'scorpio', 
                  'sagittarius', 
                  'capricorn', 
                  'aquarius', 
                  'pisces']

    if zodiac not in all_zodiac:
        return HttpResponseNotFound("Zodiac not found")

    return HttpResponse(zodiac)
