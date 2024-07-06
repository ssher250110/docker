from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from habits.models import Habit
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer
from habits.services import set_scheduler_periodicity_reminder_habit


class HabitCreateAPIView(CreateAPIView):
    """Создание привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()
        set_scheduler_periodicity_reminder_habit(habit)


class HabitListAPIView(ListAPIView):
    """Просмотр списка пользовательских привычек"""
    serializer_class = HabitSerializer

    def get_queryset(self):
        """Возвращает список привычек отфильтрованных по владельцу данных привычек"""
        user = self.request.user
        return Habit.objects.filter(owner=user)


class HabitRetrieveAPIView(RetrieveAPIView):
    """Просмотр одной привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitUpdateAPIView(UpdateAPIView):
    """Обновление одной привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitDestroyAPIView(DestroyAPIView):
    """Удаление одной привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class PublicHabitListAPIView(ListAPIView):
    """Просмотр списка публичных привычек"""
    queryset = Habit.objects.filter(is_publication=True)
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]
