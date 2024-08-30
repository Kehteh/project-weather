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

    # Initialize using the first day's temperatures
    first_day = weather_data[0]
    highest_temp = first_day[2]  # First day's max temperature
    lowest_temp = first_day[1]   # First day's min temperature
    highest_temp_date = datetime.fromisoformat(first_day[0]).strftime('%Y-%m-%d')
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

    avg_min_temp = total_min_temp / len(weather_data)
    avg_max_temp = total_max_temp / len(weather_data)

    summary = (
        f"Summary for {len(weather_data)} days:\n"
        f"Mean Minimum Temperature: {avg_min_temp:.2f}\n"
        f"Mean Maximum Temperature: {avg_max_temp:.2f}\n"
        f"Highest Temperature: {highest_temp} on {highest_temp_date}\n"
        f"Lowest Temperature: {lowest_temp} on {lowest_temp_date}"
    )
    
    return summary