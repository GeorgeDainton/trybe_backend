from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GoalSerializer
from .models import Goal
from rest_framework.permissions import IsAuthenticated


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]
