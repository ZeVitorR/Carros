# Generated by Django 5.1.4 on 2024-12-13 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_car_photo_car_plate'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cars/'),
        ),
    ]
