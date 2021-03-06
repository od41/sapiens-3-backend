# Generated by Django 3.2.13 on 2022-05-11 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0023_alter_member_beliefs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='beliefs',
            field=models.CharField(blank=True, choices=[('Christianity', 'Christianity'), ('Muslim', 'Muslim'), ('Other', 'Other')], default=None, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='interests',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]
