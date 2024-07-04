from rest_framework.serializers import ValidationError


class RelatedHabitValidator:
    """Валидатор проверки поля связанной привычки"""
    def __init__(self, field):
        self.field = field

    def __call__(self, habit):
        related_habit = habit.get(self.field)
        is_pleasant_habit = habit.get('is_pleasant_habit')
        if related_habit and is_pleasant_habit:
            raise ValidationError('У приятной привычки не может быть связанной привычки.')
        elif related_habit and not related_habit.is_pleasant_habit:
            raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки.')


class AwardHabitValidator:
    """Валидатор проверки поля вознаграждения"""

    def __init__(self, field):
        self.field = field

    def __call__(self, habit):
        award = habit.get(self.field)
        is_pleasant_habit = habit.get('is_pleasant_habit')
        related_habit = habit.get('related_habit')
        if award and is_pleasant_habit:
            raise ValidationError('У приятной привычки не может быть вознаграждения')
        elif award and related_habit:
            raise ValidationError('Нельзя одновременно выбрать связанную привычку и вознаграждение.')


class TimeCompleteHabitValidator:
    """Валидатор проверки поля времени на выполнение привычки"""

    def __init__(self, field):
        self.field = field

    def __call__(self, habit):
        time_complete = dict(habit).get(self.field)
        if isinstance(time_complete, int) and time_complete > 120:
            raise ValidationError('Время выполнения привычки должно быть не более 120 секунд.')


class PeriodicityHabitValidator:
    """Валидатор проверки поля периодичности выполнения привычки"""

    def __init__(self, field):
        self.field = field

    def __call__(self, habit):
        periodicity = dict(habit).get(self.field)
        if isinstance(periodicity, int) and periodicity < 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')
