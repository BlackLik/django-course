from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

all_zodiac = {
    'aries': "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt",
    'taurus': 'tallamcorper purus non tellus integer tincidunt',
    'gemini': " genea sagitta",
    'cancer': "consectetur adipiscing elit, sed do eiusmod tempor incididunt",
    'leo': "leo dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt",
    'virgo': "virgo ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incid",
    'libra': "libra ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incid",
    'scorpio': "scorpio ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incid",
    'sagittarius': "sagittarius is a zodiac",
    'capricorn': "capricorn ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor",
    'aquarius': "aquarius ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incid",
    'pisces': "pisces ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incid"
}


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def zodiac(request, zodiac: str):
    global all_zodiac
    if zodiac not in all_zodiac.keys():
        return HttpResponseNotFound("Zodiac not found")

    return HttpResponse(all_zodiac[zodiac])


def index_zodiac(request, index_zodiac: int):
    global all_zodiac
    zodiac_list = list(all_zodiac.keys())
    if index_zodiac not in range(len(zodiac_list)):
        return HttpResponseNotFound("Zodiac not found")

    to_respond = zodiac_list[index_zodiac]

    return HttpResponseRedirect(f"../{to_respond}/")
