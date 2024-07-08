import logging
from src.utils import create_directory, get_current_timestamp

def get_logger(logger_name):
    create_directory('logs')
    log_file_path = f"logs/{get_current_timestamp()}.log"
    setup_logging(log_file_path)
    return logging.getLogger(logger_name)

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