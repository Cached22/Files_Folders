import os
from utils import log_event, handle_error, detect_file_type, chunk_content, get_file_metadata

def traverse_directory(directory_path):
    file_list = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list

def read_file_content(file_path, chunk_size):
    file_type = detect_file_type(file_path)
    content = ''
    try:
        if file_type == 'text':
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
        elif file_type == 'pdf':
            from PyPDF2 import PdfReader
            reader = PdfReader(file_path)
            content = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
        elif file_type == 'docx':
            from docx import Document
            doc = Document(file_path)
            content = "\n".join(paragraph.text for paragraph in doc.paragraphs)
        elif file_type == 'email':
            # This is a placeholder for email file reading logic
            pass
        elif file_type == 'audio_transcript':
            # This is a placeholder for audio transcript file reading logic
            pass
        else:
            log_event(f"Unsupported file type: {file_type}", "WARNING")
            return None
    except Exception as e:
        handle_error(e, file_path)
        return None

    if len(content) > chunk_size:
        return chunk_content(content, chunk_size)
    else:
        return [content]

def process_files(directory_path, chunk_size):
    file_paths = traverse_directory(directory_path)
    file_summaries = []
    for file_path in file_paths:
        file_content_chunks = read_file_content(file_path, chunk_size)
        if file_content_chunks is not None:
            for content in file_content_chunks:
                # Placeholder for summary generation logic
                # summary = generate_summary(content)
                # Placeholder for metadata extraction
                metadata = get_file_metadata(file_path)
                file_summaries.append({
                    'metadata': metadata,
                    'summary': None  # Replace None with the actual summary
                })
    return file_summaries
