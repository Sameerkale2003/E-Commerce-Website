from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'shop\index.html')

def about(request):
    return HttpResponse ("We are about")

def contact(request):
    return HttpResponse ("We are contact")

def tracker(request):
    return HttpResponse ("We are tracker")

def search(request):
    return HttpResponse ("We are search")

def productview(request):
    return HttpResponse ("We are ProductView")

def checkout(request):
    return HttpResponse ("We are checkout")