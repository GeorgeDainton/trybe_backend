from rest_framework import serializers
from .models import Goal, AuthtokenToken, AuthUser
from django.contrib.auth.models import User



class GoalSerializer(serializers.ModelSerializer):
    # user_id = serializers.CharField(source='user.id') # read_only=False
    # owner = serializers.ReadOnlyField(source='owner.username')
    # owner = AuthUserSerializer()

    # def create(self, validated_data):
    #     return Goal.objects.create(**validated_data)

    class Meta:
        model = Goal
        fields = ('id', 'goal_description', 'created_at', 'owner')
        related_object = 'auth.user'


class AuthUserSerializer(serializers.ModelSerializer):
    # goals = serializers.PrimaryKeyRelatedField(many=True, queryset=Goal.objects.all())
    goals = GoalSerializer(many=True)

    class Meta:
        model = AuthUser
        fields = ['id', 'username', 'goals']

    def create(self, validated_data):
        goal_data = validated_data.pop("goals")
        owner = AuthUser.objects.create(**validated_data)
        Goal.objects.create(owner=owner, goal=goal_data)
        return owner

class AuthtokenTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthtokenToken
        fields = ('key', 'user_id')
