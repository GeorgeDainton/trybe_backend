from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import AuthUser, Goal, AuthtokenToken, InvitedSupporter, AcceptedSupporter
from .serializers import GoalSerializer, InvitedSupporterSerializer, AcceptedSupporterSerializer, AuthUserSerializer
from djoser.serializers import UserSerializer

class GoalAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        username = request.user
        user = AuthUser.objects.get(username=username)
        goals = Goal.objects.filter(owner=user)
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        token = request.META['HTTP_AUTHORIZATION'].replace('Token ', '')
        auth_token_entry = AuthtokenToken.objects.get(key=token)
        user_id = auth_token_entry.user_id
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
        supporter_entries = AcceptedSupporter.objects.filter(goal_id=id)
        supporters_array = []
        sup_id_arr = []
        for supporter in supporter_entries:
            sup_id_arr.append(supporter.supporter_id_id)
        print(sup_id_arr)
        sups = AuthUser.objects.filter(pk__in=sup_id_arr)
        print(sups)
        # supporter_serializer = AuthUserSerializer(data=sups, many=True)
        # if supporter_serializer.is_valid():
        #     print('valid')

        ser = AuthUser.objects.get(id=2)
        serial = AuthUserSerializer(data=ser)
        if serial.is_valid():
            print('valid2')

        # for supporter in supporter_entries:
        #     supporter_instance = (AuthUser.objects.get(id=supporter.supporter_id_id))
        #     print(supporter_instance)
        #     supporter_serializer = AuthUserSerializer(data=supporter_instance)
        #     if supporter_serializer.is_valid():
        #         print('serializer valid')
        #         supporter_serializer.save()
        #         supporters_array.append(supporter_serializer.data)
        # goal = Goal.objects.get(id=id)
        # serializer = GoalSerializer(goal)
        # print(supporters_array)
        return Response({"goal": 'none', "supporters" : "none"}, status=status.HTTP_200_OK)

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

class InvitedSupporterAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = {
          'goal_id': request.data.get('goal_id'),
          'supporter_email': request.data.get('supporter_email'),
        }
        serializer = InvitedSupporterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AcceptedSupporterAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        supporter_email = request.data.get('supporter_email')

        if InvitedSupporter.objects.filter(supporter_email=supporter_email).exists():
            supporter_entries = InvitedSupporter.objects.filter(supporter_email=supporter_email)
            serializer_array = []
            for supporter in supporter_entries:
                data = {
                    'goal_id': supporter.goal_id_id,
                    'supporter_email': supporter.supporter_email,
                    'supporter_id': request.data.get('supporter_id')
                }
                serializer = AcceptedSupporterSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    serializer_array.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer_array, status=status.HTTP_200_OK)
        return Response(
            {"response": "User doesn't support any goals"},
            status=status.HTTP_400_BAD_REQUEST
        )