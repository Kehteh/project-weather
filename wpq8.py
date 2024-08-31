import csv
from datetime import datetime


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
        f"  Minimum Temperature: {format_temperature(min_temp_c)}°C\n"
        f"  Maximum Temperature: {format_temperature(max_temp_c)}°C\n\n"
    )
    return daily_summary