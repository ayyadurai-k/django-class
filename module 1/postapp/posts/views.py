from django.shortcuts import render
from django.http.response import JsonResponse
# Create your views here.


""

# C R U D => Create , Read , Update , Delete

# Functions  - API - Application Programming Interface


def get_hello_world(request):
    data = {
        "message": "Hello , World",
        "quote": "All is well"
    }
    return JsonResponse(data)

def get_hello_world2(request):
    data = {
        "message": "Hello , World 2",
        "quote": "All is well 2"
    }
    return JsonResponse(data)

