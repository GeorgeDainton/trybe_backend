from rest_framework import serializers
from .models import Goal, AuthtokenToken, AuthUser


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('id', 'goal_description', 'created_at', 'owner')
        related_object = 'auth.user'


class AuthUserSerializer(serializers.ModelSerializer):
    # goals = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Goal.objects.all())

    class Meta:
        model = AuthUser
        fields = ('id', 'username', 'email' ) #'goals'


class AuthtokenTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthtokenToken
        fields = ('key', 'user_id')
