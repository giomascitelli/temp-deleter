import os
import shutil
import logging

# Get Windows temp directory from registry
def clean_directory(directory):
    deleted_files = []

    # Check if the deleted file is a directory or a file, deletes it and then logs the deletion
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)
        try:
            if os.path.isdir(full_path):
                shutil.rmtree(full_path)
            else:
                os.remove(full_path)
            deleted_files.append(full_path)
            logging.info(f"Deleted: {full_path}")
        except FileNotFoundError:
            logging.warning(f"File not found: {full_path}")
        except PermissionError:
            logging.warning(f"Permission denied: {full_path}")
        except Exception as e:
            logging.error(f"Error deleting {full_path}: {e}")

    return deleted_files

# Clear temp directories
def clear_temp_directories(temp_dirs):
    all_deleted_files = []
    for directory in temp_dirs:
        all_deleted_files.extend(clean_directory(directory))

    return all_deleted_files

