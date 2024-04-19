import json
import sys
from gui import initialize_gui
from file_processor import traverse_directory
from summary_generator import generate_summary
from csv_exporter import export_to_csv
from utils import log_event, handle_error

# Load configuration settings
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Set up API keys
OPENAI_API_KEY = config.get('OPENAI_API_KEY', '')
ANTHROPIC_API_KEY = config.get('ANTHROPIC_API_KEY', '')

# Check if API keys are provided
if not OPENAI_API_KEY and not ANTHROPIC_API_KEY:
    print("API key for OpenAI or Anthropic is required.")
    sys.exit(1)

# Select the API based on user preference
api_selection = config['api_selection']

# Initialize the GUI
initialize_gui()

# Callback function to start processing
def start_processing(directory):
    try:
        # Traverse the directory and get all files
        files = traverse_directory(directory)

        # Process each file and generate summaries
        summaries = []
        for file in files:
            content = read_file_content(file)
            summary = generate_summary(content, api_selection)
            summaries.append(summary)

        # Export summaries to CSV
        export_to_csv(summaries, config['output_csv_name'])

        log_event("Processing completed successfully.")
    except Exception as e:
        handle_error(e)

# This is the entry point of the application
if __name__ == '__main__':
    # The GUI will call start_processing when the user initiates the process
    pass  # GUI event loop will be here, which will call start_processing when appropriate