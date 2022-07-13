from rest_framework import serializers
from djoser.serializers import UserSerializer
from .models import Goal, AuthtokenToken, AuthUser, InvitedSupporter, AcceptedSupporter


class AcceptedSupporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcceptedSupporter
        fields = ('id', 'goal_id', 'supporter_email', 'supporter_id')

class GoalSerializer(serializers.ModelSerializer):
    # supporters = serializers.PrimaryKeyRelatedField(many=True, allow_null=True, read_only=False, queryset=AcceptedSupporter.objects.all())

    class Meta:
        model = Goal
        fields = ('id', 'goal_description', 'created_at', 'owner') 
        # related_object = AcceptedSupporter


class AuthUserSerializer(UserSerializer):
    class Meta:
        model = AuthUser
        fields = ('id', 'username', 'email')


class AuthtokenTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthtokenToken
        fields = ('key', 'user_id')


class InvitedSupporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitedSupporter
        fields = ('id', 'goal_id', 'supporter_email')


