import csv
from datetime import datetime

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
        f"5 day overview/n"
        f"  The lowest temperature will be {lowest_temp:.1f}°C, and will occur on {lowest_temp_date}.\n"
        f"  The highest temperature will be {highest_temp:.1f}°C, and will occur on {highest_temp_date}.\n"
        f"  The average low this week is {ave_min_temp:.1f}°C.\n"
        f"  The average high this week is {ave_max_temp:.1f}°C.\n"
    )
    
    return summary