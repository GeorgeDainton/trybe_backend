from rest_framework.test import APITestCase
from rest_framework import status
from trybe_api.models import Goal

class GoalApiTest(APITestCase):
    def test_get_goal_list(self):
        payload = {'goal_description': 'Do something else'}
        self.client.post('/goals/', payload, format='json')
        res = self.client.get('/goals/')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Goal.objects.count(), 1)

    def test_create_goal(self):
        payload = {'goal_description': 'Do homework'}
        res = self.client.post('/goals/', payload, format='json')

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Goal.objects.count(), 1)
        self.assertEqual(Goal.objects.get().goal_description, 'Do homework')

    def test_delete_goal(self):
        payload = {'goal_description': 'Do something else'}
        self.client.post('/goals/', payload, format='json')
        res = self.client.delete('/goals/1/')

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Goal.objects.count(), 0)

    def test_update_goal(self):
        payload = {'goal_description': 'Do something else'}
        payload2 = {'goal_description': 'Have a rest'}
        self.client.post('/goals/', payload, format='json')
        res = self.client.put('/goals/1/', payload2, format='json')

        self.assertEqual(res.status_code, status.HTTP_200_OK)