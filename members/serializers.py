from dataclasses import field
from email.mime import image
from django.forms import CharField
from rest_framework import serializers
from connect_app.models import Connection, Message, HouseListing, HomeListingImages
from members import models


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes our user profile object"""
    # interests = serializers.SlugRelatedField(
    #     # many=True,
    #     # read_only=True,
    #     slug_field='interests',
    #     queryset=models.Interest.objects.all()
    #  )

     
    class Meta:
        model = models.Member
        fields = ('id', 'first_name', 'username', 'last_name', 'email', 'password', 'preferred_location', 'age', 'budget', 'display_photo', 'gender', 'education_level', 'interests', 'beliefs', 'description', 'occupation')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
    def create(self, validated_data):
        """Create and return new user"""
        user = models.Member.objects.create_user(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            username = validated_data['username'],
            last_name = validated_data['last_name'],
            password = validated_data['password'],
            # display_photo =validated_data['display_photo']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class MessageSerializer(serializers.ModelSerializer):
    """For Serializing Message"""

    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=models.Member.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=models.Member.objects.all())
    
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']


class HomeListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeListingImages
        fields = ('upload', 'house_listing')


class HouseListingSerializer(serializers.ModelSerializer):
     photo_upload = HomeListingImageSerializer(many=True, source='house_listing_houselistingimage', read_only=True)
     class Meta:
        model = HouseListing
        fields = ('location', 'rooms', 'price', 'tenure', 'user', 'description', 'photo_upload')
        read_only_fields= ('photo_upload',)


class ConnectWithAUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = ['sender', 'receiver', 'accepted', 'rejected','timestamp']



    
      
    #     def get(self, request, *args, **kwargs):
    #     allOrders = Order.objects.all()
    #     args = {"allOrders": allOrders}
    #     return render(request, self.template_name, args)

    # def post(self, request):
    #     orderId = self.request.GET.get("order_id")
    #     statusAccept = self.request.GET.get("acceptButton")
    #     statusReject = self.request.GET.get("rejectButton")