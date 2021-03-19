from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    title = models.CharField('Название статьи', max_length=100)
    text = models.TextField('Текст статьи')
    date = models.DateTimeField('Дата и время', default=timezone.now)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
