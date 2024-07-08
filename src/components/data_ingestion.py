import pandas as pd
from pymongo import MongoClient
from src.exception import CustomException

def ingest_data_from_mongodb(uri, db_name, collection_name):
    try:
        # Connect to MongoDB
        client = MongoClient(uri)
        db = client[db_name]
        collection = db[collection_name]
        
        # Load data into a DataFrame
        data = list(collection.find())
        df = pd.DataFrame(data)
        
        # Drop the MongoDB `_id` field if it exists
        if '_id' in df.columns:
            df.drop('_id', axis=1, inplace=True)
            
        return df
    except Exception as e:
        raise CustomException("Error in ingesting data from MongoDB", e)