# Generated by Django 3.2.13 on 2022-05-07 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect_app', '0003_homelistingimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='houselisting',
            name='photo_upload',
            field=models.ManyToManyField(related_name='houselisting_image', to='connect_app.HomeListingImages'),
        ),
    ]
