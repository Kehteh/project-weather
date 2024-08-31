import csv
from datetime import datetime

def generate_summary(weather_data):
#     """Outputs a summary for the given weather data.

#     Args:
#         weather_data: A list of lists, where each sublist represents a day of weather data.
#     Returns:
#         A string containing the summary information.
#     """
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

