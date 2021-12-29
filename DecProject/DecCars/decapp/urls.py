from django.urls import path
from DecCars.decapp.views import test_response, test_heading

urlpatterns = [
    path('test/', test_response),
    path('tests/', test_heading),
]
