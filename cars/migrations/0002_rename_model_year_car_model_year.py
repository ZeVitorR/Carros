# Generated by Django 5.1.4 on 2024-12-12 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='Model_year',
            new_name='model_year',
        ),
    ]
