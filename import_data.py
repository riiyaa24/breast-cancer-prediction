from sklearn.datasets import load_breast_cancer
from pymongo import MongoClient
import pandas as pd
from src.exception import CustomException
from src.logger import get_logger
from src.utils import create_directory, get_current_timestamp

logger = get_logger(__name__)

def load_data_to_mongodb(uri, db_name, collection_name):
    try:
        logger.info("Starting the data loading process")

        # Load the breast cancer dataset from sklearn
        logger.info("Loading the breast cancer dataset from sklearn")
        breast_cancer = load_breast_cancer()
        data = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
        data['target'] = breast_cancer.target

        # Connect to MongoDB
        logger.info("Connecting to MongoDB")
        client = MongoClient(uri)
        db = client[db_name]
        collection = db[collection_name]

        # Insert data into MongoDB
        logger.info("Inserting data into MongoDB")
        collection.insert_many(data.to_dict('records'))

        logger.info("Data loading process completed successfully")
    except Exception as e:
        logger.error(f"Error in loading data to MongoDB: {e}")
        raise CustomException("Error in loading data to MongoDB", e)

if __name__ == "__main__":
    # Define MongoDB connection details
    uri = "mongodb://localhost:27017/"
    db_name = "your_database"
    collection_name = "your_collection"

    # Load data to MongoDB
    try:
        load_data_to_mongodb(uri, db_name, collection_name)
        logger.info("Data loaded to MongoDB successfully")
    except CustomException as e:
        logger.error(f"An error occurred: {e}")
