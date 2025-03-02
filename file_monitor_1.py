import hashlib
import os
import sys
import logging
import time

# Configure logging
logging.basicConfig(filename="file_changes.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Function to calculate the hash of a file
def calculate_hash(file_path):
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None
    except PermissionError:
        print(f"Permission denied: {file_path}")
        return None
    except IsADirectoryError:
        print(f"Expected a file but found a directory: {file_path}")
        return None
    except OSError as e:
        with open("error_log.txt", "a") as log_file:
            log_file.write(f"OS error while reading {file_path}: {e}\n")
        print(f"OS error while reading {file_path}. Details logged.")
        return None

# Function to monitor files for changes
def monitor_files(file_list, interval=2):
    if not file_list:
        print("No valid files provided for monitoring. Exiting.")
        logging.info("No valid files provided for monitoring. Exiting.")
        return
    
    file_hashes = {file: calculate_hash(file) for file in file_list if os.path.isfile(file)}
    print("Monitoring files for changes... Press Ctrl+C to stop.")
    logging.info("Monitoring started for files: %s", ", ".join(file_list))
    
    try:
        while True:
            for file in file_list:
                if os.path.isfile(file):
                    new_hash = calculate_hash(file)
                    if new_hash and new_hash != file_hashes.get(file):
                        message = f"File modified: {file}"
                        print(message)
                        logging.info(message)
                        file_hashes[file] = new_hash
                elif file in file_hashes:
                    message = f"File deleted: {file}"
                    print(message)
                    logging.info(message)
                    del file_hashes[file]
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
        logging.info("Monitoring stopped by user.")

# Take file names from user input or command-line arguments
if len(sys.argv) > 1:
    files_to_monitor = sys.argv[1:]
else:
    user_input = input("Enter file names to monitor (comma-separated): ").strip()
    files_to_monitor = [file.strip() for file in user_input.split(',') if file.strip()]

monitor_files(files_to_monitor)
