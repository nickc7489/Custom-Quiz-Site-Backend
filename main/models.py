from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=1000, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    questions = models.JSONField()
    author = models.CharField(max_length=1000, blank=True)
    username = models.CharField(max_length=1000, blank=True)
    attempts = models.JSONField(blank=True, default=list)
