from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('connect', views.ConnectsList, name='connects_list'),
]