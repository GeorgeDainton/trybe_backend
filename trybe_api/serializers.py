from rest_framework import serializers
from .models import Goal, AuthtokenToken, AuthUser, InvitedSupporter, AcceptedSupporter


class AcceptedSupporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcceptedSupporter
        fields = ('id', 'goal_id', 'supporter_email', 'supporter_id')


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('id', 'goal_description', 'created_at', 'owner') 


class AuthUserSerializer(serializers.ModelSerializer):
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
