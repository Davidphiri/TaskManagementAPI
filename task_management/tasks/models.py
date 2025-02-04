from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

TASK_STATUS = (
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('in_progress', 'In Progress'),
)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    priority_level = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=TASK_STATUS, default='pending')

