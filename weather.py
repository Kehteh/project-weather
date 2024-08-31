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

    date_list = []
    min_list = []
    max_list = []

    for day in weather_data:
        date_list.append(convert_date(day[0]))
        min_list.append(convert_f_to_c(day[1]))
        max_list.append(convert_f_to_c(day[2]))

    min_value, min_position = find_min(min_list)
    max_value, max_position = find_max(max_list)

    mean_min_list = calculate_mean(min_list)
    mean_max_list = calculate_mean(max_list)

    num_days = len(weather_data)


    summary = (
        f"{num_days} Day Overview\n"
        f"  The lowest temperature will be {min_value:.1f}°C, and will occur on {date_list[min_position]}.\n"
        f"  The highest temperature will be {max_value:.1f}°C, and will occur on {date_list[max_position]}.\n"
        f"  The average low this week is {mean_min_list:.1f}°C.\n"
        f"  The average high this week is {mean_max_list:.1f}°C.\n"
        )
    return summary




def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summary = ""

    for data in weather_data:
        date = data[0]
        min_temp_c = convert_f_to_c(float(data[1]))
        max_temp_c = convert_f_to_c(float(data[2]))
        daily_summary += (
            f"---- {convert_date(date)} ----\n"
            f"  Minimum Temperature: {format_temperature(min_temp_c)}\n"
            f"  Maximum Temperature: {format_temperature(max_temp_c)}\n\n"
        )
    return daily_summary
