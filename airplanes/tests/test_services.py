import math

from django.test import TestCase

from ..services import flight_time, fuel_capacity, fuel_consumption_per_min


class TestAirplaneCapacity(TestCase):
    def test_total_fuel_capacity(self):
        airplane_id = 2
        expected_capacity = 400
        calculated_capacity = fuel_capacity(airplane_id=airplane_id)
        self.assertEqual(expected_capacity, calculated_capacity)

    def test_total_fuel_capacity_with_zero_id(self):
        airplane_id = 0
        expected_capacity = 0
        calculated_capacity = fuel_capacity(airplane_id=airplane_id)
        self.assertEqual(expected_capacity, calculated_capacity)


class TestAirplaneConsumption(TestCase):
    airplane_id = 4
    no_of_passengers = 1000
    base_consumption_multiplication = 0.80  # defined in requirements
    base_consumption_per_min = round(math.log(airplane_id)*base_consumption_multiplication, 3)
    single_passenger_consumption = 0.002   # defined in requirement
    passengers_consumption_per_min = round(single_passenger_consumption*no_of_passengers, 3)

    def test_zero_consumption(self):
        airplane_id = 1
        no_of_passengers = 0
        expected_consumption = 0
        calculated_consumption = fuel_consumption_per_min(
            airplane_id=airplane_id,
            no_of_passengers=no_of_passengers
        )
        self.assertEqual(expected_consumption, calculated_consumption)
        self.assertFalse(calculated_consumption)

    def test_passenger_consumption_per_min_with_zero_id(self):
        airplane_id = 0
        expected_consumption = self.passengers_consumption_per_min
        calculated_consumption = fuel_consumption_per_min(
            airplane_id=airplane_id,
            no_of_passengers=self.no_of_passengers
        )
        self.assertEqual(expected_consumption, calculated_consumption)

    def test_passenger_consumption_per_min_with_zero_base_consumption(self):
        airplane_id = 1
        expected_consumption = self.passengers_consumption_per_min
        calculated_consumption = fuel_consumption_per_min(
            airplane_id=airplane_id,
            no_of_passengers=self.no_of_passengers
        )
        self.assertEqual(expected_consumption, calculated_consumption)

    def test_base_consumption_per_min_with_no_passengers(self):
        no_of_passengers = 0
        expected_consumption = self.base_consumption_per_min
        calculated_consumption = fuel_consumption_per_min(
            airplane_id=self.airplane_id,
            no_of_passengers=no_of_passengers
        )
        self.assertEqual(expected_consumption, calculated_consumption)

    def test_consumption_per_min_with_valid_id_and_valid_passengers(self):
        expected_consumption = self.base_consumption_per_min + self.passengers_consumption_per_min
        calculated_consumption = fuel_consumption_per_min(
            airplane_id=self.airplane_id,
            no_of_passengers=self.no_of_passengers
        )
        self.assertEqual(expected_consumption, calculated_consumption)


class TestAirplaneFlightTime(TestCase):
    def test_flight_time_with_zero_consumption(self):
        total_fuel_capacity = 400
        total_consumption_per_min = 0
        expected_flight_time = math.inf
        calculated_flight_time = flight_time(
            total_fuel=total_fuel_capacity,
            consumption_per_min=total_consumption_per_min,
        )
        self.assertEqual(calculated_flight_time, expected_flight_time)

    def test_flight_time_with_no_fuel(self):
        total_fuel_capacity = 0
        total_consumption_per_min = 50
        expected_flight_time = 0
        calculated_flight_time = flight_time(
            total_fuel=total_fuel_capacity,
            consumption_per_min=total_consumption_per_min,
        )
        self.assertEqual(calculated_flight_time, expected_flight_time)

    def test_flight_time_with_zero_fuel_and_zero_consumption(self):
        total_fuel_capacity = 0
        total_consumption_per_min = 0
        expected_flight_time = math.inf
        calculated_flight_time = flight_time(
            total_fuel=total_fuel_capacity,
            consumption_per_min=total_consumption_per_min,
        )
        self.assertEqual(calculated_flight_time, expected_flight_time)

    def test_flight_time_with_valid_fuel_and_valid_consumption(self):
        total_fuel_capacity = 400
        total_consumption_per_min = 50
        expected_flight_time = 8.0
        calculated_flight_time = flight_time(
            total_fuel=total_fuel_capacity,
            consumption_per_min= total_consumption_per_min,
        )
        self.assertEqual(calculated_flight_time, expected_flight_time)
