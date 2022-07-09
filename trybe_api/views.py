from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GoalSerializer
from .models import Goal

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [permissions.DjangoModelPermissions]
