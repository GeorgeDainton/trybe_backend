from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GoalSerializer
from .serializers import UserSerializer
from .models import Goal
from django.contrib.auth.models import User

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer