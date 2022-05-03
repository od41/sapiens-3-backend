# Generated by Django 3.2.13 on 2022-05-03 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20220503_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='banner_photo',
            field=models.ImageField(blank=True, default='members/default_bp.jpg', null=True, upload_to='members/'),
        ),
        migrations.AlterField(
            model_name='member',
            name='display_photo',
            field=models.ImageField(blank=True, default='members/default_dp.jpg', null=True, upload_to='members/'),
        ),
    ]