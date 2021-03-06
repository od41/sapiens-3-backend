from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from members import models, serializers
from rest_framework import viewsets
from rest_framework.authtoken.views  import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.settings import api_settings

# class MemberApiView(APIView):
#     def post

# class HelloApiView(APIView):

#     myApiList = [
#         "Users in the app"
#         "Users in the same location"
#         "People searching for roomies to corent aspace"
#     ]

#     def get(self, request, format=None):
#         return Response({'message': "Hello world", "an_apiview":myApiList})


class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.Member.objects.all()



class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'newkey': 'here'})






    
# create an account
# login
# get users
# search users
# update user
# match user
