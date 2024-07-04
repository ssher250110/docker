from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import TimeCompleteHabitValidator, PeriodicityHabitValidator, RelatedHabitValidator, \
    AwardHabitValidator


class HabitSerializer(ModelSerializer):
    """Сериализатор модели привычки"""
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            TimeCompleteHabitValidator(field='time_complete'),
            PeriodicityHabitValidator(field='periodicity'),
            RelatedHabitValidator(field='related_habit'),
            AwardHabitValidator(field='award')
        ]
