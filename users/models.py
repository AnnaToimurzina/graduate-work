from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=100, verbose_name='First name')
    last_name = models.CharField(max_length=100, verbose_name='Last name')
    job_title = models.CharField(max_length=500, verbose_name='Title job')
    birth_date = models.DateField(null=True, blank=True)
    notes = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.job_title}"

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
