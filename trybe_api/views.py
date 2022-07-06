import imp
from django.http import QueryDict
from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets 

from .serializers import GoalSerializer
from .models import Goal

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

   