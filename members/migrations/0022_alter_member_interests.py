# Generated by Django 3.2.13 on 2022-05-11 11:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0021_auto_20220511_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='interests',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=600, null=True), size=None),
        ),
    ]
