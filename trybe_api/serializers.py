from rest_framework import serializers
from .models import Goal, AuthtokenToken, AuthUser, Supporter, Messages


class GoalSerializer(serializers.ModelSerializer):
    supporters = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Supporter.objects.all())

    class Meta:
        model = Goal
        fields = ('id', 'goal_description', 'created_at', 'owner', 'supporters')
        # related_object = 'auth.user'


class AuthUserSerializer(serializers.ModelSerializer):
    # goals = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Goal.objects.all())

    class Meta:
        model = AuthUser
        fields = ('id', 'username', 'email' ) #'goals'


class AuthtokenTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthtokenToken
        fields = ('key', 'user_id')


class SupporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supporter
        fields = ('id', 'goal_id', 'supporter_email', 'supporter_accepted', 'supporter_id')


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('id', 'goal_id', 'sender_id', 'message', 'created_at')