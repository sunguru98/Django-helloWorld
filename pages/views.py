from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def indexPageView(request):
    return HttpResponse("<h1>HELLO TO DJANGO !!!!</h1>")
