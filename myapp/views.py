from django.shortcuts import render
from django.http import HttpResponse

def function(request):
    return HttpResponse("<h1>Hello world!</h1>")
