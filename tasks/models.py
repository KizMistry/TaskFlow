from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Task(models.Model):
    """
    Task model, related to User and Project
    """
    priority_choices = [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')]
    status_choices = [('todo', 'ToDo'), ('in progress', 'In Progress'), ('completed', 'Completed')]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    task_priority = models.CharField(max_length=10, choices=priority_choices, default='medium')
    task_status = models.CharField(max_length=20, choices=status_choices, default='todo')
    file = models.FileField(upload_to='media/', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.task