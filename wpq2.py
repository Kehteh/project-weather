# import csv
# from datetime import datetime

def convert_f_to_c(temp_in_fahrenheit):
#     """Converts a temperature from Fahrenheit to Celcius.

#     Args:
#         temp_in_fahrenheit: float representing a temperature.
#     Returns:
#         A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
#     """



#     temp_in_celcius = float(temp_in_fahrenheit) - 32 / 1.8
#     return round(temp_in_celcius,1)

# my way ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



# The correct way :

    return round((float(temp_in_fahrenheit) - 32)* 5/9 , 1)