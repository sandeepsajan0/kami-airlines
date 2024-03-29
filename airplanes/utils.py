import math


def convert_decimal_to_min(decimal: float) -> str:
    if decimal is math.inf:
        return str(decimal)
    minutes = int(decimal)
    seconds = int((decimal*60) % 60)
    return f"{minutes}.{seconds}"
