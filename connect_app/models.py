from django.conf import settings
from django.db import models
from django.utils import timezone

class Profile(models.Model):
    # Constants
    GENDER_C = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")
    ]

    ED_LEVEL_C = [
        ("Secondary", "Secondary"),
        ("Post-Secondary", "Post-Secondary"),
        ("Univeristy", "Univeristy"),
        ("Masters", "Masters"),
        ("PhD", "PhD"),
    ]

    BELIEFS_C = [
        ("Christianity", "Christianity"),
        ("Muslim", "Muslim"),
        ("Other", "Other"),
    ]

    INTERESTS_C = []

    # class fields
    full_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=timezone.now)
    age = models.IntegerField(null=True)
    preferred_location = models.CharField(max_length=300, null=True)
    gender = models.CharField(
        max_length=50, blank=True, null=True, choices=GENDER_C)
    display_photo = models.ImageField(
        upload_to='display_photo', default='default_display_photo.jpg', null=True, blank=True)
    banner_photo = models.ImageField(
        upload_to='banner_photo', default='default_banner_photo.jpg', null=True, blank=True)
    description = models.TextField(null=True, max_length=400)
    education_level = models.CharField(
        max_length=20, choices=ED_LEVEL_C, default=None, null=True, blank=True)
    occupation = models.CharField(
        max_length=500, null=True)
    beliefs = models.CharField(
        max_length=12, choices=BELIEFS_C, default=None, null=True, blank=True)
    preferred_address = models.CharField(max_length=600, blank=True, null=True)
    # interests = models.ManyToOneRel(
        # INTERESTS_C, related_name='interests')
    # liked_apartments = models.ManyToOneRel(
    #     INTERESTS_C, related_name='liked_apartments', blank='true')
    # favourites = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL, related_name='favourites', blank='true')
    # rejected_connections = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL, related_name='rejected_connections', blank='true')

    # email
    # age
    # prefered location
    # gender
    # display photo
    # banner photo
    # description
    # education
    # occupation
    # beliefs
    # interests
    # address
    # favourites
    # connections
    # rejected_connections
    # liked apartments

    def connect(self):
        # do something
        print("connect profile")

    def __str__(self) -> str:
        return super().__str__()
