from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def ex1(request):
    return HttpResponse("Hello World !")