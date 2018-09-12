from django.urls import path

from . import views
from django.conf.urls.i18n import urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
]