from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Goal
from .serializers import GoalSerializer

class GoalAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        goals = Goal.objects.all()
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            # 'id': request.data.get('id'), # work in progress
            'goal_description': request.data.get('goal_description'),
        }
        serializer = GoalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GoalDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id, *args, **kwargs):
        goal = Goal.objects.get(id=id)
        serializer = GoalSerializer(goal)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id, *args, **kwargs):
        if Goal.objects.filter(id=id).exists():
            goal = Goal.objects.get(id=id)
            goal.delete()
            return Response(
                {"response": "Goal Deleted", "goal_id": id}, 
                status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {"res": "Goal Doesn't Exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self, request, id, *args, **kwargs):
        if Goal.objects.filter(id=id).exists():
            goal = Goal.objects.get(id=id)
            data = {
              'goal_description': request.data.get('goal_description'),
            }
            serializer = GoalSerializer(instance=goal, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"res": "Project Doesn't Exist"},
            status=status.HTTP_400_BAD_REQUEST
        )