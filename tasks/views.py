from django.db.models import Q, Count
from django.db.models import Count, F, Case, When, Value, CharField
from django.db.models.functions import Coalesce, Concat
from rest_framework import viewsets, generics
from rest_framework.response import Response

from users.models import User


from .models import Task
from .serializers import TaskSerializer, ImpotSerializer, ImportantTaskWithUsersSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ImportantTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        # Получаем все задачи, которые не взяты в работу
        # и от которых зависят другие задачи, взятые в работу
        return Task.objects.filter(
            status='pending',  # Задачи, которые не взяты в работу
            executor=None,  # Задачи без executor
            parent_task__isnull=False  # Задачи, у которых parent_task не равен None
        )

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ImpotSerializer

class ImportantTasksView(generics.ListAPIView):
    serializer_class = ImportantTaskWithUsersSerializer

    def get_queryset(self):
        # Получаем все задачи, которые не взяты в работу
        # и от которых зависят другие задачи, взятые в работу
        important_tasks = Task.objects.filter(
            status='pending',  # Задачи, которые не взяты в работу
            executor=None,  # Задачи без executor
            parent_task__isnull=False  # Задачи, у которых parent_task не равен None
        )

        # Собираем информацию о задачах с сроками и соответствующих сотрудниках
        result_list = []
        for task in important_tasks:
            executor_names = self.get_executor_names(task)
            result_list.append({
                'task_name': task.task_name,
                'deadline': task.deadline,
                'executor_names': executor_names
            })

        return result_list

    def get_executor_names(self, task):
        # Получаем имена сотрудников, связанных с задачей
        executor_names = []
        if task.parent_task:
            # Если задача имеет родительскую задачу, добавляем исполнителя этой задачи
            if task.parent_task.executor:
                executor_names.append(f"{task.parent_task.executor.first_name} {task.parent_task.executor.last_name}")

        # Добавляем имена исполнителей подзадач
        subtasks = Task.objects.filter(parent_task=task, status='pending', executor__isnull=False)
        for subtask in subtasks:
            executor_names.append(f"{subtask.executor.first_name} {subtask.executor.last_name}")

        return executor_names