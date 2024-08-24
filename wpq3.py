import csv
from datetime import datetime

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # temperature = []

    # for index in range(len(temperature)):
    # temperature[index] = temperature[index] 

    weather_data_float = []
    for item in weather_data:
        weather_data_float.append(float(item))

    mean = float(sum(weather_data_float) / len(weather_data_float)) 
    return mean
