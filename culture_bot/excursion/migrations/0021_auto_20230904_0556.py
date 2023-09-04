# Generated by Django 2.2.19 on 2023-09-04 05:56

from django.db import migrations, models
import excursion.validators


class Migration(migrations.Migration):

    dependencies = [
        ('excursion', '0020_auto_20230901_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audioexhibit',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, validators=[excursion.validators.html_validator], verbose_name='Описание аудио'),
        ),
        migrations.AlterField(
            model_name='descriptionexhibit',
            name='text',
            field=models.TextField(help_text='каждая область - это отдельное сообщение которые будут идти с задержкой пропорционально длине текста, ', validators=[excursion.validators.html_validator], verbose_name='Текст сообщения'),
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='address',
            field=models.CharField(max_length=200, validators=[excursion.validators.html_validator], verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='answer_for_reflection',
            field=models.TextField(blank=True, null=True, validators=[excursion.validators.html_validator], verbose_name='Ответ для рефлексии'),
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='author',
            field=models.CharField(max_length=50, validators=[excursion.validators.html_validator], verbose_name='Художник'),
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='name',
            field=models.CharField(max_length=200, validators=[excursion.validators.html_validator], verbose_name='Название экспоната'),
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='question_for_reflection',
            field=models.TextField(blank=True, null=True, validators=[excursion.validators.html_validator], verbose_name='Вопрос для рефлексии'),
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='where_start',
            field=models.TextField(blank=True, null=True, validators=[excursion.validators.html_validator], verbose_name='Как пройти к экспонату'),
        ),
        migrations.AlterField(
            model_name='photoexhibit',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, validators=[excursion.validators.html_validator], verbose_name='Описание фотографии'),
        ),
        migrations.AlterField(
            model_name='reflectionexhibit',
            name='author',
            field=models.CharField(max_length=20, validators=[excursion.validators.html_validator], verbose_name='Комментатор'),
        ),
        migrations.AlterField(
            model_name='reflectionexhibit',
            name='contact',
            field=models.CharField(max_length=50, validators=[excursion.validators.html_validator]),
        ),
        migrations.AlterField(
            model_name='reflectionexhibit',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, validators=[excursion.validators.html_validator], verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='route',
            name='description',
            field=models.TextField(validators=[excursion.validators.html_validator], verbose_name='Описание маршрута'),
        ),
        migrations.AlterField(
            model_name='route',
            name='lyrics',
            field=models.TextField(default='', validators=[excursion.validators.html_validator], verbose_name='Лирическое описание'),
        ),
        migrations.AlterField(
            model_name='route',
            name='question_end',
            field=models.TextField(blank=True, null=True, validators=[excursion.validators.html_validator], verbose_name='Вопрос в конце маршрута'),
        ),
        migrations.AlterField(
            model_name='route',
            name='title',
            field=models.CharField(max_length=50, validators=[excursion.validators.html_validator], verbose_name='Название маршрута'),
        ),
        migrations.AlterField(
            model_name='route',
            name='where_start',
            field=models.TextField(validators=[excursion.validators.html_validator], verbose_name='Как пройти к старту'),
        ),
        migrations.AlterField(
            model_name='videoexhibit',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, validators=[excursion.validators.html_validator], verbose_name='Описание видео'),
        ),
    ]
