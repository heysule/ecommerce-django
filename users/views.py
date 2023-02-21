from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User

def login(request):
    return HttpResponse('<h1>Login Successful</h1>')

def register(request):
    return JsonResponse({
        "id": 34,
        "email": "suleiman@email.com",
        "auth_token": "sdfsdglirgg",
        "phone": "08012345678",
    })

def template_ninja(request):
    return render(request, 'index.html')