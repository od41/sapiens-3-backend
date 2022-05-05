from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()  #instantiate the router

router.register(r'profile', UserProfileViewset)


urlpatterns = [
    # path('register/', UserProfileViewset.as_view(), name='register'),
    path('api-auth/', include('rest_framework.urls')),
    # path('api-view/', HelloApiView.as_view(), name= 'view' ),
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls))
   
]