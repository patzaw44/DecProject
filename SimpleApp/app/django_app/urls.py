
# from rest_framework import routers
# from django.urls import include, path
# from .views import CarsViewSet
#
# router = routers.DefaultRouter()
# router.register(r'', CarsViewSet)
# urlpatterns = [
#     path('', include(router.urls)),
# #     # path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework'))
# ]

from django.urls import path

# from .views import CarsDataView


# app_name = "Cars"
#
# # app_name will help us do a reverse look-up latter.
# urlpatterns = [
#     path('cars/', CarsDataView),
# ]

from rest_framework.routers import SimpleRouter
from .views import CarsDataViewSet
    # SpeciesViewSet
from django.urls import include, path

router = SimpleRouter()
router.register("", CarsDataViewSet, basename="django_app")
urlpatterns = router.urls
# router = routers.DefaultRouter()
# router.register(r'species', SpeciesViewSet)



