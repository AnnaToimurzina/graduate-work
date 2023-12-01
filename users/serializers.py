
from rest_framework import serializers

from tasks.models import Task
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class BusyUserSerializer(serializers.ModelSerializer):
    count_active_tasks = serializers.SerializerMethodField()

    def get_count_active_tasks(self, user):
        # Подсчет активных задач пользователя
        active_tasks_count = Task.objects.filter(
            executor=user,
            status__in=['pending', 'processing']
        ).count()

        return active_tasks_count

    class Meta:
        model = User
        fields = ['count_active_tasks', 'first_name', 'last_name']



