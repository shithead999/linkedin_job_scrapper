import csv
import os
from dataclasses import asdict

def write_to_csvs(job, company, detail):
    # Function to write or append to a CSV file
    def write_to_csv(file_name, data):
        file_exists = os.path.isfile(file_name) and os.path.getsize(file_name) > 0
        with open(file_name, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)

    # Convert dataclass objects to dictionaries
    job_dict = asdict(job)
    company_dict = asdict(company)
    detail_dict = asdict(detail)

    # Write or append each dictionary to its respective CSV file
    write_to_csv('job.csv', job_dict)
    write_to_csv('company.csv', company_dict)
    write_to_csv('detail.csv', detail_dict)


def get_start_value(file_path):
    # Check if file exists and is not empty
    if os.path.isfile(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            last_row = None
            for row in reader:
                if row:  # Check if row is not empty
                    last_row = row
            if last_row:
                return int(last_row[0])+1  # Convert first column of last row to integer
    return 1  # Default value if file doesn't exist or is empty