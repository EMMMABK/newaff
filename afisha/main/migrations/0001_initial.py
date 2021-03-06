# Generated by Django 4.0.5 on 2022-06-19 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя режиссёра:')),
            ],
            options={
                'verbose_name': 'Режиссёр',
                'verbose_name_plural': 'Режиссёры',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название:')),
                ('description', models.TextField(verbose_name='Информация про фильм')),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.director', verbose_name='Режиссёр')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100, verbose_name='Отзывы:')),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.movie', verbose_name='Фильм')),
            ],
            options={
                'verbose_name': 'Предосмотр',
                'verbose_name_plural': 'Предосмотры',
            },
        ),
    ]
