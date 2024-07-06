from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """Отображение информации о привычке в админ панели"""
    list_display = ['id', 'owner', 'location', 'time', 'action', 'is_pleasant_habit', 'related_habit', 'periodicity',
                    'award', 'time_complete', 'is_publication']
