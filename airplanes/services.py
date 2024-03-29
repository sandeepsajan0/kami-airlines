import math


def fuel_consumption_per_min(airplane_id, no_of_passengers):
    base_consumption_per_min = (math.log(airplane_id))*0.80
    passengers_consumption_per_min = 0.002*int(no_of_passengers)
    total_consumption_per_min = round(base_consumption_per_min + passengers_consumption_per_min, 3)
    return total_consumption_per_min


def fuel_capacity(airplane_id):
    return 200*int(airplane_id)


def airplane_flight_time(total_fuel, consumption_per_min):
    if consumption_per_min:
        flight_time = round(total_fuel/consumption_per_min, 2)
        return flight_time
    return math.inf
