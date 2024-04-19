import os
import mimetypes
import logging

# Initialize logging
logging.basicConfig(filename='log_file_name', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def log_event(message, level):
    if level == 'info':
        logging.info(message)
    elif level == 'warning':
        logging.warning(message)
    elif level == 'error':
        logging.error(message)

def handle_error(error_message, exception=None):
    log_event(error_message, 'error')
    if exception:
        log_event(str(exception), 'error')

def detect_file_type(file_path):
    file_type, _ = mimetypes.guess_type(file_path)
    return file_type or 'unknown'

def get_file_metadata(file_path):
    try:
        file_stats = os.stat(file_path)
        file_size = file_stats.st_size
        creation_date = file_stats.st_ctime
        folder_path, file_name = os.path.split(file_path)
        subdirectory_path = os.path.dirname(folder_path)
        file_type = detect_file_type(file_path)
        return {
            'folder_path': folder_path,
            'subdirectory_path': subdirectory_path,
            'file_name': file_name,
            'file_type': file_type,
            'file_size': file_size,
            'creation_date': creation_date
        }
    except Exception as e:
        handle_error(f"Error getting metadata for file: {file_path}", e)
        return None

def format_insights(insights, format_type='bullet_points'):
    if format_type == 'bullet_points':
        return '\n'.join(f'- {insight}' for insight in insights)
    elif format_type == 'numbered':
        return '\n'.join(f'{index + 1}. {insight}' for index, insight in enumerate(insights))
    else:
        return ' '.join(insights)