import requests
from django.conf import settings

from habits.models import Habit
from users.models import User


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


def send_notification_habit(habit_id):
    habit = Habit.objects.get(pk=habit_id)
    if habit.owner.tg_id:
        message = f'{}'