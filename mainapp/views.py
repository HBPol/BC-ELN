from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Instruments

def index(request):
    
    page_title = 'Application Index'
    instruments_table = Instruments.objects.all()
    
    context = {
        'page_title': page_title,
        'instruments_table': instruments_table,
    }
    
    return render(request, 'mainapp/index.html', context)

def details(request):
    
    page_title = 'Application Index'
    instruments_table = Instruments.objects.all()
    
    context = {
        'page_title': page_title,
        'instruments_table': instruments_table,
    }
    
    return render(request, 'mainapp/index.html', context)
