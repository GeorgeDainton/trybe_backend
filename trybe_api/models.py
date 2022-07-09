from tkinter import CASCADE
from django.db import models
from trybe_backend import settings
from django.contrib.auth.models import User

class Goal(models.Model):
    goal_description = models.CharField(max_length=180)

    def __str__(self):
        return self.goal_description
