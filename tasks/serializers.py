from rest_framework import serializers
from tasks.models import Task
from users.models import User


class TaskSerializer(serializers.ModelSerializer):
    is_important = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'

    def get_is_important(self, task):
        return task.status == 'pending' and (task.parent_task is None or task.parent_task.status == 'processing')


class ImportantSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'job_title']


class ImportantTaskWithUsersSerializer(serializers.Serializer):
    task_name = serializers.CharField()
    deadline = serializers.DateField()
    executor_names = serializers.ListField(child=serializers.CharField())

    class Meta:
        fields = ['task_name', 'deadline', 'executor_names']
