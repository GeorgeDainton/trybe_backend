from django.db import models

class Goal(models.Model):
    goal_description = models.CharField(max_length=180)

    def __str__(self):
        return self.goal_description

class OwnerModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True

