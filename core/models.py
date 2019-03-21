from __future__ import unicode_literals
from datetime import datetime
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, max_length=280)
    created_at = models.DateField(auto_now_add=True, blank=True)
    completed = models.BooleanField(default=False)
    completed_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
