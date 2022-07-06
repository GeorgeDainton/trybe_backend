from django.db import models

# Create your models here.
class Goal(models.Model):
    goal_description = models.CharField(max_length=180)

    def __str__(self):
        return self.goal_description
