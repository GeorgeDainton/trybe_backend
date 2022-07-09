from rest_framework import serializers

from .models import Goal
from django.contrib.auth.models import User


class GoalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goal
        fields = ('id', 'goal_description')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')