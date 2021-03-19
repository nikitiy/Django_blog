# Generated by Django 3.1.7 on 2021-03-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название статьи')),
                ('text', models.TextField(verbose_name='Текст статьи')),
                ('date', models.DateTimeField(verbose_name='Дата и время')),
                ('fwfdw', models.TextField()),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
