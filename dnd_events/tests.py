from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import DNDEvent


class DNDEventListViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='test'
        )
        self.other_user = User.objects.create_user(
            username='otheruser', password='othertest'
        )

        self.dnd_event_data = {
            'game_name': 'Test Game',
            'game_description': 'Test Description',
            'owner': self.user
        }

    def test_user_logged_in_can_list_dnd_events(self):
        self.client.force_login(self.user)
        response = self.client.get('/dnd_events/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DNDEventModelTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='annauser', password='test'
        )

    def test_create_dnd_event(self):
        dnd_event_data = {
            'game_name': 'DND Test Game',
            'game_description': 'DND test Description',
            'owner': self.user,
        }
        initial_count = DNDEvent.objects.count()

        dnd_event = DNDEvent.objects.create(**dnd_event_data)

        self.assertEqual(DNDEvent.objects.count(), initial_count + 1)
        self.assertEqual(dnd_event.game_name, 'DND Test Game')
