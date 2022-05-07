# from telnetlib import Telnet
# from tkinter import Y
from django.conf import settings

from members.models import Member
from django.db import models

class Message(models.Model):
    sender = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1500)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    def __str__(self):
           return self.message
    class Meta:
           ordering = ('timestamp',)
    

class HouseListing(models.Model):   
    location = models.CharField(max_length=100)
    rooms = models.IntegerField(default=0)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    tenure = models.IntegerField()
    user = models.ForeignKey(Member,on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    # photo_upload = models.ManyToManyField(HomeListingImages, related_name="houselisting_image")


class HomeListingImages(models.Model):
    house_listing = models.ForeignKey(HouseListing, on_delete=models.CASCADE, null=True, related_name='house_listing_houselistingimage')
    upload = models.ImageField(upload_to='connect/%Y/%m/%d/', default='connect/default_bp.jpg', null=True, blank=True)

    