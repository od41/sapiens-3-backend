# Generated by Django 3.2.13 on 2022-05-11 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0027_alter_member_interests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='interests',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
