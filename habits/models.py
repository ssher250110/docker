from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    """Модель привычки"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                              verbose_name='Создатель привычки',
                              help_text='Укажите создателя привычки')
    location = models.CharField(max_length=100, **NULLABLE, verbose_name='Место выполнения привычки',
                                help_text='Укажите место выполнения привычки')
    time = models.TimeField(verbose_name='Время выполнения привычки', help_text='Укажите время выполнения привычки')
    action = models.CharField(max_length=150, verbose_name='Действие привычки', help_text='Укажите действие привычки')
    is_pleasant_habit = models.BooleanField(default=False, verbose_name='Приятная привычка',
                                            help_text='Укажите, приятная ли привычка')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE,
                                      verbose_name='Связанная привычка',
                                      help_text='Укажите связанную привычку')
    periodicity = models.PositiveIntegerField(default=1, verbose_name='Периодичность выполнения привычки',
                                              help_text='Укажите периодичность выполнения привычки')
    award = models.CharField(max_length=150, **NULLABLE, verbose_name='Вознаграждение',
                             help_text='Укажите вознаграждение')
    time_complete = models.PositiveIntegerField(default=1, verbose_name='Время на выполнение привычки',
                                                help_text='Укажите время на выполнение привычки')
    is_publication = models.BooleanField(default=False, verbose_name='Признак публикации',
                                         help_text='Укажите признак публикации')

    def __str__(self):
        return f'Привычка: {self.action}, в {self.time}, место: {self.location}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ['location', ]
