from rest_framework.serializers import ValidationError


class TimeCompleteHabitValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time_complete = value.get(self.field)
        if time_complete > 120:
            raise ValidationError('Время выполнения привычки должно быть не более 120 секунд.')


class PeriodicityHabitValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        periodicity = value.get(self.field)
        if periodicity < 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')


