from django.shortcuts import  render
from django.http import HttpResponse
from DecCars.decapp.models import Auto


def test_response(request):
    return HttpResponse("Cars app")


def test_heading(request):
    auto_all = Auto.objects.all()
    # number = len(auto_all)
    return render(request, 'auto.html', {'text': auto_all})
