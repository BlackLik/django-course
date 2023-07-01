from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class HomeView(View):
    def get(self, request):
        return HttpResponse("Hello, world")
    
class PostView(View):
    def get(self, request, name_post: str):
        return HttpResponse(f"Name {name_post}")
    
class PostDetailView(View):
    def get(self, request, id_post: int):
        return HttpResponse(f"Id {id_post}")