from django.db import models
from users.models import User

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    parent_task = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    executor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='task_executor')
    deadline = models.DateField()
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('processing', 'В процессе'),
        ('completed', 'Завершено'),
        ('failed', 'Не удалось')]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')



    def __str__(self):
        return f"{self.task_name} {self.executor} {self.deadline}"

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


