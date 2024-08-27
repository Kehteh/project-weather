import csv
from datetime import datetime

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()

    data = []


    for item in weather_data:
        try:
            data.append(float(item))
        except ValueError:
            continue


    max_value = data[0]
    max_index = 0
    for index in range (len(data)):
        if data[index] >= min_value:
            max_value = data[index]
            max_index = index

    return max_value, max_index