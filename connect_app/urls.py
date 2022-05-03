from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('connect', views.MatchedMembersList, name='connects_list'),
]