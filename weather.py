import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    
    date = datetime.fromisoformat(iso_string)
    readable_date = date.strftime("%A %d %B %Y")
    return readable_date




def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    return round((float(temp_in_fahrenheit) - 32)* 5/9 , 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    weather_data_float = []
    for item in weather_data:
        weather_data_float.append(float(item))

    mean = float(sum(weather_data_float) / len(weather_data_float)) 
    return mean


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    with open(csv_file) as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        for row in reader:
            if row: 
                # Convert min and max to integers
                data.append([row[0], int(row[1]), int(row[2])])
    
    return data




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
        if data[index] >= max_value:
            max_value = data[index]
            max_index = index

    return max_value, max_index


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    if not weather_data:
        return "no data available"
    
    # variables
    highest_temp = weather_data[0][2]
    lowest_temp = weather_data[0][1]
    highest_temp_date = datetime.fromisoformat(weather_data[0][0]).strftime('%Y-%m-%d')
    lowest_temp_date = highest_temp_date

    total_min_temp = 0
    total_max_temp = 0

    for day in weather_data:
        date_str, min_temp, max_temp = day
        date = datetime.fromisoformat(date_str).strftime('%Y-%m-%d')
        
        total_min_temp += min_temp
        total_max_temp += max_temp
        
        if max_temp > highest_temp:
            highest_temp = max_temp
            highest_temp_date = date
        
        if min_temp < lowest_temp:
            lowest_temp = min_temp
            lowest_temp_date = date

    ave_min_temp = total_min_temp / len(weather_data)
    ave_max_temp = total_max_temp / len(weather_data)

    summary = (
        f"  The lowest temperature will be {lowest_temp:.1f}°C, and will occur on {lowest_temp_date}.\n"
        f"  The highest temperature will be {highest_temp:.1f}°C, and will occur on {highest_temp_date}.\n"
        f"  The average low this week is {ave_min_temp:.1f}°C.\n"
        f"  The average high this week is {ave_max_temp:.1f}°C.\n"
    )
    
    return summary






def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
