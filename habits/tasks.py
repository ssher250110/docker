from celery import shared_task

from habits.services import sending_reminder_habit


@shared_task
def reminder_habit(habit_id):
    """Отложенная задача, напоминания выполнения привычки"""
    sending_reminder_habit(habit_id)
