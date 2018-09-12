from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.context_processors import request

def index(request):
    return HttpResponse ("<h1>This is the welcome page.</h1>")