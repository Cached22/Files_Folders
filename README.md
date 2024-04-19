# File Summarizer App

## Overview
This Python application recursively goes through all the files and subfolders within a specified directory, summarizes each file into key insights, and exports the summaries to a CSV file. It supports various file types and chunks larger files to fit within the model's context window.

## Features
- Recursive file processing
- Support for text, PDF, Word, email, and audio transcript files
- Content chunking for large files
- Insight extraction using GPT-4 Turbo or Claude 3 Opus
- CSV export with metadata and summaries
- Customizable insight count and formatting
- Selective processing with filters
- Parallel processing for efficiency
- Progress tracking and user interface
- Comprehensive logging and error handling
- API integration capabilities

## Installation
1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt` in your terminal.

## Configuration
Edit the `config.json` file to set your preferences for:
- `api_selection`: Choose between "OpenAI" or "Anthropic".
- `file_types`: Specify the types of files to process.
- `chunk_size`: Set the size for content chunking.
- `insight_count`: Define the number of insights to extract.
- `output_csv_name`: Name your output CSV file.
- `output_directory`: Set the directory for the output CSV.
- `log_file_name`: Name your log file.

## Usage
1. Run `main.py` to start the application.
2. Use the GUI to select the directory you wish to process.
3. Configure the options as needed.
4. Click the 'Start' button to begin processing.
5. The results will be saved in the specified output directory as a CSV file.

## Troubleshooting
If you encounter any issues:
- Check the `log_file_name` for error messages.
- Ensure that you have the correct API keys set for your chosen model.
- Verify that the file types you are trying to process are supported.
- Make sure you have the necessary permissions to read the files and write to the output directory.

For more help, refer to the FAQs or contact support.

## License
This software is released under the MIT License. See the `LICENSE` file for more details.