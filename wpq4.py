import csv
from datetime import datetime

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
    