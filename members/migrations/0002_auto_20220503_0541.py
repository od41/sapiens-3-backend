# Generated by Django 3.2.13 on 2022-05-03 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='banner_photo',
            field=models.ImageField(blank=True, default='default_banner_photo.jpg', null=True, upload_to='banner_photo'),
        ),
        migrations.AddField(
            model_name='member',
            name='beliefs',
            field=models.CharField(blank=True, choices=[('Christianity', 'Christianity'), ('Muslim', 'Muslim'), ('Other', 'Other')], default=None, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='description',
            field=models.TextField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='display_photo',
            field=models.ImageField(blank=True, default='default_display_photo.jpg', null=True, upload_to='display_photo'),
        ),
        migrations.AddField(
            model_name='member',
            name='education_level',
            field=models.CharField(blank=True, choices=[('Secondary', 'Secondary'), ('Post-Secondary', 'Post-Secondary'), ('Univeristy', 'Univeristy'), ('Masters', 'Masters'), ('PhD', 'PhD')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='occupation',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='preferred_address',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='preferred_location',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='interests',
            field=models.ManyToManyField(help_text='Your interests, for matching you to your co-tenant', related_name='interests', to='members.Interests'),
        ),
    ]
