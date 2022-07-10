from django.db import models
from django.contrib.auth.models import User

class AuthUser(models.Model): ## work in progress
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class Goal(models.Model):
    goal_description = models.CharField(max_length=180)
    # user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.goal_description


class AuthtokenToken(models.Model): # work in progress
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(User, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'