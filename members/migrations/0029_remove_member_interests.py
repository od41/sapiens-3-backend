# Generated by Django 3.2.13 on 2022-05-11 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0028_alter_member_interests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='interests',
        ),
    ]
