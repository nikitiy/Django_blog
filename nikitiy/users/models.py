from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    gender = (
        ('T', 'Trance'),
        ('M', 'Man'),
        ('W', 'Woman')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField('Фото пользователя', default='default.png', upload_to='user_images')
    choice = models.BooleanField('Просто галочка :3', default=False)
    genderChoice = models.CharField(max_length=1, choices=gender, default='T')

    def __str__(self):
        return f'Профайл пользователя { self.user }'

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'
