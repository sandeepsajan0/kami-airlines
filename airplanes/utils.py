import math


def convert_decimal_to_min(decimal):
    if decimal is math.inf:
        return decimal
    minutes = int(decimal)
    seconds = int((decimal*60) % 60)
    return f"{minutes}.{seconds}"
