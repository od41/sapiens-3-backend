from django.shortcuts import render
from django.views import generic

def HomeView(request):
    return render(request, 'general/home.html', {})



def ConnectsList(request):
    return render(request, 'connect_app/connects_list.html', {})