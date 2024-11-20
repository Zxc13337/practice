import os
import time

def get_file_creation_time(file_path):
    return time.ctime(os.path.getctime(file_path))

def format_file_size(size_in_bytes):
    for unit in ['байт', 'КБ', 'МБ', 'ГБ']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024
