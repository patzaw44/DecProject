from django.shortcuts import  render
from django.http import HttpResponse

def test_response(request):
    return HttpResponse("Cars app")
