from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.


class HomeView(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the home page.")


def get_rectangle_area(request, width, height):
    return HttpResponse(f"The area of the rectangle is {width * height}")


def get_square_area(request, width):
    return HttpResponse(f"The area of the square is {width * width}")


def get_circle_area(request, radius):
    return HttpResponse(f"The area of the circle is {3.14 * radius ** 2}")
