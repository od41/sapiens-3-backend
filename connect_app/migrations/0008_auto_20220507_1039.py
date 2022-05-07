# Generated by Django 3.2.13 on 2022-05-07 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('connect_app', '0007_homelistingimages_house_listing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homelistingimages',
            name='username',
        ),
        migrations.AlterField(
            model_name='homelistingimages',
            name='house_listing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='house_listing_houselistingimage', to='connect_app.houselisting'),
        ),
    ]
