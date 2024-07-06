import json

import requests
from django.conf import settings
from django_celery_beat.models import IntervalSchedule, PeriodicTask

from habits.models import Habit


def set_scheduler_periodicity_reminder_habit(habit):
    """Функция создания периодической задачи для отправки напоминания о привычке"""
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=habit.periodicity,
        period=IntervalSchedule.DAYS,
    )
    PeriodicTask.objects.create(
        interval=schedule,
        name=f'Periodicity reminder habit: habit_id {habit.pk}, owner {habit.owner}',
        task='habits.tasks.reminder_habit',
        kwargs=json.dumps({
            'habit_id': habit.pk,
        })
    )


def sending_reminder_habit(habit_id):
    """Функция отправки напоминания о привычке"""
    habit = Habit.objects.get(pk=habit_id)
    if habit.owner.tg_id:
        message = (f'Выполнить: {habit.action}, в {habit.time},'
                   f'место выполнения: {habit.location if habit.location else 'не указано'}')
        send_telegram_message(habit.owner.tg_id, message)


def send_telegram_message(chat_id, message):
    """Функция отправки сообщения в телеграм."""
    params = {
        "text": message,
        "chat_id": chat_id,
    }
    requests.get(
        f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN_BOT}/sendMessage",
        params=params,
    )
