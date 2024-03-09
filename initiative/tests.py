from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import DNDInitiative


class DNDInitiativeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='annauser', password='test'
        )

    def test_create_dnd_initiative(self):
        initiative_data = {
            'name': 'DND Test Initiative',
            'initiative': 10,
            'owner': self.user,
        }
        initiative = DNDInitiative.objects.create(**initiative_data)

        self.assertEqual(initiative.name, 'DND Test Initiative')
        self.assertIsInstance(initiative.initiative, int)


