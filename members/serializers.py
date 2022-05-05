from django.forms import CharField
from rest_framework import serializers
from members import models


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes our user profile object"""
     
    class Meta:
        model = models.Member
        fields = ('id', 'first_name', 'username', 'last_name', 'email', 'password', 'preferred_location', 'age', 'budget')
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
            password = validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)