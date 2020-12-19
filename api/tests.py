from django.test import TestCase
from rest_framework.test import APIClient

from .models import User, BookingList, Workplace


class ApiTest(TestCase):

    def setUp(self):

        self.client = APIClient()
        self.password = '12345'
        self.user = User.objects.create_user(
            username='user',
            password=self.password,
        )
        self.workplace = Workplace.objects.create(
            cabinet_number=7
        )
        self.booking = BookingList.objects.create(
            author=self.user,
            workplace=self.workplace,
            datetime_from='2020-01-01T00:00:00',
            datetime_to='2021-01-01T00:00:00'
        )

    def test_auth(self):

        data = {
            'username': self.user.username,
            'password': self.password,
        }
        responce = self.client.post('/api/v1/token/', data)
        self.assertEqual(responce.status_code, 200,
                         msg='Problem with auth')
        self.assertTrue(responce.data['access'], msg='Token problem')

    def test_workplace(self):

        self.client.force_authenticate(user=self.user)
        responce = self.client.get('/api/v1/workplaces/')
        self.assertEqual(responce.status_code, 200)
        self.assertContains(responce, self.workplace)

        responce = self.client.get(f'/api/v1/workplaces/{self.workplace.pk}/')
        self.assertEqual(responce.status_code, 200)
        self.assertContains(responce, self.booking)

    def test_booking(self):

        self.client.force_authenticate(user=self.user)
        responce = self.client.get('/api/v1/booking/')
        origin_len = len(responce.data)
        self.assertEqual(responce.status_code, 200)
        self.assertContains(responce, self.booking)

        data = {
            'workplace': self.workplace,
            'datetime_from': '2020-01-01T00:00:00',
            'datetime_to': '2021-01-01T00:00:00',
        }

        responce = self.client.post('/api/v1/booking/', data)
        self.assertEqual(responce.status_code, 400)
        responce = self.client.get('/api/v1/booking/')
        self.assertNotContains(responce, data)

        data = {
            'workplace': self.workplace,
            'datetime_from': '2021-01-02T00:00:00',
            'datetime_to': '2022-01-01T00:00:00',
        }

        responce = self.client.post('/api/v1/booking/', data)
        self.assertEqual(responce.status_code, 201)
        responce = self.client.get('/api/v1/booking/')
        responce_len = len(responce.data)
        self.assertNotEqual(origin_len, responce_len)
        self.assertContains(responce, data['datetime_from'])
        self.assertContains(responce, data['datetime_to'])
