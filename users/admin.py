from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Отображение информации о пользователях в админ панели"""
    list_display = ['id', 'email', 'phone', 'country', 'tg_id']
