from django.db import models
from django.contrib.auth.models import User


class Status(models.TextChoices):
    PENDING = 'pending', 'Pending'
    IN_PROGRESS = 'in progress', 'In Progress'


class Priority(models.IntegerChoices):
    LOW = 1, 'Low'
    MEDIUM = 2, 'Medium'
    HIGH = 3, 'High'

class TaskModel(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    status = models.CharField(max_length=20,choices=Status.choices, default=Status.PENDING)
    priority = models.IntegerField(choices=Priority.choices,default=Priority.MEDIUM)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='tasks')


    def __str__(self):
        return self.title