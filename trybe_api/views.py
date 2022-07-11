from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

from .models import Goal, AuthtokenToken
from .serializers import AuthUserSerializer, GoalSerializer, AuthtokenTokenSerializer

class GoalAPIView(APIView):
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        if 'HTTP_AUTHORIZATION' in request.META: 
            token = request.META['HTTP_AUTHORIZATION'].replace('Token ', '')
            # Token 188dd58b04a44b93391df19145d9ccc41c8dac81
            auth_token_entry = AuthtokenToken.objects.get(key=token)
            user_id = auth_token_entry.user_id
            goals = Goal.objects.filter(id=user_id)
            serializer = GoalSerializer(goals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"response": "Authorization Token not provided"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        # if 'HTTP_AUTHORIZATION' in request.META: 
        token = request.META['HTTP_AUTHORIZATION'].replace('Token ', '')
        auth_token_entry = AuthtokenToken.objects.get(key=token)
        user_id = auth_token_entry.user_id
        print(user_id)
        # user_serializer = AuthUserSerializer(data={id: user_id})

        data = {
            'goal_description': request.data.get('goal_description'),
            'owner': user_id,
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
                {"response": "Goal Doesn't Exist"},
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
            {"response": "Goal Doesn't Exist"},
            status=status.HTTP_400_BAD_REQUEST
        )