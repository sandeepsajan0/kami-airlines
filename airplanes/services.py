import math


def fuel_consumption_per_min(airplane_id: int, no_of_passengers: int) -> float:
    base_consumption_per_min = (math.log(airplane_id))*0.80 if airplane_id > 0 else 0
    passengers_consumption_per_min = 0.002*int(no_of_passengers)
    total_consumption_per_min = round(base_consumption_per_min + passengers_consumption_per_min, 3)
    return total_consumption_per_min


def fuel_capacity(airplane_id: int) -> int:
    return 200*int(airplane_id)


def flight_time(total_fuel: int, consumption_per_min: float) -> float:
    return round(total_fuel/consumption_per_min, 2) if consumption_per_min else math.inf
