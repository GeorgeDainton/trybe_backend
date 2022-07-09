from rest_framework import serializers
from .models import Goal

class GoalSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Goal
        fields = ('id', 'goal_description', 'owner')
