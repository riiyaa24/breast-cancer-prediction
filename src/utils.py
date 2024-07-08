import os
import json
from datetime import datetime
import logging

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        logging.info(f"Directory {path} created successfully.")
    else:
        logging.info(f"Directory {path} already exists.")

def save_json(data, file_path):
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f)
        logging.info(f"Data saved to {file_path} successfully.")
    except Exception as e:
        logging.error(f"Error saving data to {file_path}: {e}")

def load_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        logging.info(f"Data loaded from {file_path} successfully.")
        return data
    except Exception as e:
        logging.error(f"Error loading data from {file_path}: {e}")
        return None

def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def setup_logging(log_file_path):
    logging.basicConfig(filename=log_file_path,
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filemode='w')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)
    logging.info("Logging setup complete.")
