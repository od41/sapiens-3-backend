# Generated by Django 3.2.13 on 2022-05-08 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_alter_member_education_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='preferred_address',
            new_name='current_address',
        ),
    ]
