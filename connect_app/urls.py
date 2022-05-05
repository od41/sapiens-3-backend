from django.urls import path
from connect_app.views import *


urlpatterns = [
    path('connect', matchedMembersList),
]