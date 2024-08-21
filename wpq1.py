import csv
from datetime import datetime

"""Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

def convert_date(iso_string):
    date = datetime.fromisoformat(iso_string)
    readable_date = date.strftime("%A %d %B %Y")
    return readable_date