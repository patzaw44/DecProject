from django.shortcuts import render
from django.http import HttpResponse
from .models import Cars


def desktop(request):
    question = Cars.objects.all()
    return HttpResponse(question)

