from django.contrib import admin
from django.urls import path
from DecCars.decapp.views import test_response

from . import decapp
from .decapp import urls
from django.conf.urls import include
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_response)
]