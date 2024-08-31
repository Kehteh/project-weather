import csv
from datetime import datetime
import weather

weather_data = [
    ["2020-06-19T07:00:00+08:00", 47, 46],
    ["2020-06-20T07:00:00+08:00", 51, 67],
    ["2020-06-21T07:00:00+08:00", 58, 72],
    ["2020-06-22T07:00:00+08:00", 59, 71],
    ["2020-06-23T07:00:00+08:00", 52, 71],
    ["2020-06-24T07:00:00+08:00", 52, 67],
    ["2020-06-25T07:00:00+08:00", 48, 66],
    ["2020-06-26T07:00:00+08:00", 53, 66]
]

date_list = []
min_list = []
max_list = []

for day in weather_data:
    date_list.append(weather.convert_date(day[0]))
    min_list.append(weather.convert_f_to_c(day[1]))
    max_list.append(weather.convert_f_to_c(day[2]))

print(date_list)
print(min_list)
print(max_list)

min_value, min_position = weather.find_min(min_list)
max_value, max_position = weather.find_max(max_list)

mean_min_list = weather.calculate_mean(min_list)
mean_max_list = weather.calculate_mean(max_list)

print(min_value)
print(min_position)

print(max_value)
print(max_position)

summary = (
    f"5 day overview\n"
    f"  The lowest temperature will be {min_value:.1f}°C, and will occur on {date_list[min_position]}.\n"
    f"  The highest temperature will be {max_value:.1f}°C, and will occur on {date_list[max_position]}.\n"
    f"  The average low this week is {mean_min_list:.1f}°C.\n"
    f"  The average high this week is {mean_max_list:.1f}°C.\n"
)

print(summary)