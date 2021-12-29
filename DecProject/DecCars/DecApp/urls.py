from urllib import request
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from rest_framework import routers
from DecCars.DecApp import views
from .views import create_car
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()
router.register(r'cars', views.CarViewSet, 'Car data')
router.register(r'carss', views.CarDelViewSet, 'Deltest')
router.register(r'rate', views.RateViewSet, 'Ratetest')
router.register(r'carsall', views.AllCarsViewSet, 'All Cars')
router.register(r'popular', views.PopularCarsViewSet, 'Popular cars')

urlpatterns = [
    # path('test/', test_heading),
    # path('cars', csrf_exempt(create_car)),
    re_path(r'^', include(router.urls))
]
