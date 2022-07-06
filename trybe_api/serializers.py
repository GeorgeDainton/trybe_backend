from rest_framework import serializers

from .models import Goal

class GoalSerializer(serializers.HyperlinkedModelSerializzer):
    class Meta:
        model = Goal
        fields = ('id', 'goal_description')