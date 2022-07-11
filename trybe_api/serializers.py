from rest_framework import serializers
from .models import Goal, AuthtokenToken, AuthUser
from django.contrib.auth.models import User

class GoalSerializer(serializers.ModelSerializer):
    # user_id = serializers.CharField(source='user.id') # read_only=False
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        return Goal.objects.create(**validated_data)

    class Meta:
        model = Goal
        fields = ('id', 'goal_description', 'created_at', 'owner')
        related_object = 'user'

class AuthtokenTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthtokenToken
        fields = ('key', 'user_id')

class UserSerializer(serializers.ModelSerializer):
    goals = serializers.PrimaryKeyRelatedField(many=True, queryset=Goal.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'goals']