from django.urls import path
from . import views

urlpatterns = [
    path('connect', views.connects_list, name='connects_list'),
]