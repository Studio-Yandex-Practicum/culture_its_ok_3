# Generated by Django 2.2.19 on 2023-08-29 19:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursion', '0002_reflectionexhibit_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibit',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='rating',
            field=models.IntegerField(default=1, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='reflectionexhibit',
            name='rating',
            field=models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
