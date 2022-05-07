from django.urls import path
from connect_app.views import *


urlpatterns = [
    path('connect', matchedMembersList),
    # URL form : "/api/messages/1/2"
    path('api/messages/<int:sender>/<int:receiver>', message_list, name='message-detail'),  # For GET request.
    # URL form : "/api/messages/"
    path('api/messages/', message_list, name='message-list'),   # For POST
    path('upload/', upload, name='upload'),  # For POST
    
]