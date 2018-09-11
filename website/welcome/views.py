from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.context_processors import request

def index(request):
    return HttpResponse ("This is the welcome page.")