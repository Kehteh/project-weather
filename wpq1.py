import csv
from datetime import datetime

def convert_date(iso_string):
    date = datetime.fromisoformat(iso_string)
    readable_date = date.strftime("%A %d %B %Y")
    return readable_date