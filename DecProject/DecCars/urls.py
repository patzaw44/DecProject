from django.contrib import admin
from django.urls import include, path
from DecApp import urls
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls))
]