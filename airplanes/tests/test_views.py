import json

from django.test import TestCase
from rest_framework import status
from unittest.mock import patch


class TestAirplaneCapacityView(TestCase):

    def test_view_with_post_method_invalid_data(self):
        request_data = [
            {"id": 0, "passengers": 100},   # id should be >0
            {"id": 2, "passengers": 200},
        ]

        response = self.client.post('/airplanes/capacity/', json.dumps(request_data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        request_data = [
            {"id": 1, "passengers": 100},
            {"id": 2, "passengers": -1},    # passenger should be >=0
        ]

        response = self.client.post('/airplanes/capacity/', json.dumps(request_data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        request_data = [
            {"id": 1, "passengers": 100},
            {"id": 2},
        ]

        response = self.client.post('/airplanes/capacity/', json.dumps(request_data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        request_data = [
            {"id": 1, "passengers": 100},
            {"passengers": 200},
        ]

        response = self.client.post('/airplanes/capacity/', json.dumps(request_data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('airplanes.views.fuel_consumption_per_min')
    @patch('airplanes.views.flight_time')
    @patch('airplanes.views.fuel_capacity')
    def test_view_with_post_method_and_valid_data(self, mock_fuel_capacity, mock_flight_time, mock_fuel_consumption_per_min):
        mock_fuel_capacity.return_value = 2000
        mock_flight_time.return_value = 120
        mock_fuel_consumption_per_min.return_value = 20

        request_data = [
            {"id": 1, "passengers": 100},
            {"id": 2, "passengers": 200},
            {"id": 3, "passengers": 300}
        ]

        response = self.client.post('/airplanes/capacity/', json.dumps(request_data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

        expected_data = [
            {"id": 1, "consumption_per_min": "20 litre/minute", "airplane_flight_time": "120.0 minutes"},
            {"id": 2, "consumption_per_min": "20 litre/minute", "airplane_flight_time": "120.0 minutes"},
            {"id": 3, "consumption_per_min": "20 litre/minute", "airplane_flight_time": "120.0 minutes"}
        ]
        self.assertEqual(response.data, expected_data)

    def test_view_with_invalid_method(self):

        response = self.client.get('/airplanes/capacity/', content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.put('/airplanes/capacity/', content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
