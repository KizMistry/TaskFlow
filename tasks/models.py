from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Task(models.Model):
    """
    Task model, related to User and Project
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    file = models.FileField(upload_to='media/', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.task