from rest_framework import serializers
from .models import Goal, AuthtokenToken, AuthUser, InvitedSupporter, AcceptedSupporter


class GoalSerializer(serializers.ModelSerializer):
    # supporters = serializers.PrimaryKeyRelatedField(many=True, allow_null=True, read_only=False, queryset=AcceptedSupporter.objects.all())

    class Meta:
        model = Goal
        fields = ('id', 'goal_description', 'created_at', 'owner') #, 'supporters'
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


class InvitedSupporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitedSupporter
        fields = ('id', 'goal_id', 'supporter_email')

class AcceptedSupporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcceptedSupporter
        fields = ('id', 'goal', 'supporter_email', 'supporter')
