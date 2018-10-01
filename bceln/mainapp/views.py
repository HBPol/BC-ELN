from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is the main application view!</h1>")