import os
import datetime

# Directory to search for .html files
search_dir = r'C:\Users'

# Date range to filter files
start_date = datetime.datetime(2024, 7, 4)
end_date = datetime.datetime(2024, 7, 7)

# Function to check if file was created within the specified date range
def is_within_date_range(file_path, start_date, end_date):
    creation_time = os.path.getctime(file_path)
    creation_date = datetime.datetime.fromtimestamp(creation_time)
    return start_date <= creation_date <= end_date

# Iterate over files in the directory
for root, dirs, files in os.walk(search_dir):
    # Check if the root directory contains \AppData\, then skip it
    if '\\AppData\\' in root:
        continue
    
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            if is_within_date_range(file_path, start_date, end_date):
                print(file_path)
