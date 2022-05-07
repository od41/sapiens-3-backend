# Generated by Django 3.2.13 on 2022-05-07 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('connect_app', '0002_houselisting'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeListingImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(default='connect/default_bp.jpg', null=True, upload_to='connect/%Y/%m/%d/')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lister', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]