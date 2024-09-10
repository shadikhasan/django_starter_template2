from django.http import HttpResponse
from django.shortcuts import render

def testapp(request):
    return HttpResponse("Hello, world!")
