import csv
from datetime import datetime

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()

    data = []


    for item in weather_data:
        try:
            data.append(float(item))
        except ValueError:
            continue


    min_value = data[0]
    min_index = 0
    for index in range (len(data)):
        if data[index] <= min_value:
            min_value = data[index]
            min_index = index

    return min_value, min_index