import csv
import os
from utils import log_event, LOG_ERROR

def export_to_csv(data, output_directory, output_csv_name):
    """
    Exports the given data to a CSV file.

    :param data: List of dictionaries containing file metadata and summaries.
    :param output_directory: The directory where the CSV file will be saved.
    :param output_csv_name: The name of the CSV file to be saved.
    """
    try:
        # Ensure the output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Define the path for the CSV file
        csv_file_path = os.path.join(output_directory, output_csv_name)

        # Define the CSV column headers
        fieldnames = [
            'folder_path',
            'subdirectory_path',
            'file_name',
            'file_type',
            'summary'
        ]

        # Write the data to the CSV file
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for entry in data:
                writer.writerow(entry)

        log_event(f"CSV export successful. File saved to: {csv_file_path}", "INFO")

    except Exception as e:
        log_event(f"Failed to export CSV: {e}", LOG_ERROR)