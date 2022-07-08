from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from trybe_api.serializers import GoalSerializer
from trybe_api.models import Goal

# get_goals_url = reverse('goals')
# create_url = reverse('goals')

# def sample_payload():
#     payload = {
#       "goal_description" : "Do homework"
#     }
#     return Goal.objects.create(**payload)


class GoalApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_goal_list(self):
        res = self.client.get('/goals/')

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_goal(self):
        payload = {
          "goal_descrption": "Do homework"
        }

        res = self.client.post('/goals/', payload)
        print(res)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(res.data, {'id': {'\d'}, 'goal_description': 'Do homework'})
