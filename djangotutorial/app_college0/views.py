from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse(render(request, "app_college0/Landing.jsx"))
