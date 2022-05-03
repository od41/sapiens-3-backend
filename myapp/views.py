# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. This is Slim's app There. for Home page")

def home(request):
    return render(request,'myapp/base.html')