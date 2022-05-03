# Generated by Django 3.2.13 on 2022-05-03 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_rename_interests_interest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='banner_photo',
            field=models.ImageField(blank=True, default='gallery/members/default_bp.jpg', null=True, upload_to='gallery/members/'),
        ),
        migrations.AlterField(
            model_name='member',
            name='display_photo',
            field=models.ImageField(blank=True, default='gallery/members/default_dp.jpg', null=True, upload_to='gallery/members/'),
        ),
    ]
