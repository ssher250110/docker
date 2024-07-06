from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта', help_text='Введите электронную почту')
    phone = models.CharField(max_length=15, **NULLABLE, verbose_name='Телефон', help_text='Введите номер телефона')
    country = models.CharField(max_length=85, **NULLABLE, verbose_name='Страна', help_text='Введите название страны')
    avatar = models.ImageField(upload_to='users/avatar', **NULLABLE, verbose_name='Аватар',
                               help_text='Загрузите аватар')
    tg_id = models.CharField(max_length=50, **NULLABLE, verbose_name='id телеграм чата',
                             help_text='Укажите id телеграм чата')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['email', ]
