from django.test import TestCase
from trybe_api import models

class ModelTest(TestCase):
    def test_goal_model_str(self):
        goal = models.Goal.objects.create(
          goal_description = "Do homework"
        )

        self.assertEqual(str(goal), goal.goal_description)