# Generated by Django 3.1.7 on 2021-03-17 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='choice',
            field=models.BooleanField(default=False, verbose_name='Поддерживает ли Путина?'),
        ),
    ]
