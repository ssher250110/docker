from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from habits.models import Habit
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitListAPIView(ListAPIView):
    serializer_class = HabitSerializer

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(owner=user)


class HabitRetrieveAPIView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class PublicHabitListAPIView(ListAPIView):
    queryset = Habit.objects.filter(is_publication=True)
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]
