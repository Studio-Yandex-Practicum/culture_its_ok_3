# Generated by Django 2.2.19 on 2023-08-30 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('excursion', '0006_remove_route_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exhibit',
            name='order',
        ),
    ]
