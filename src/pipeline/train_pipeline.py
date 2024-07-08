from src.components.data_ingestion import ingest_data_from_mongodb
from src.components.data_transformation import transform_data
from src.components.model_trainer import train_model, evaluate_model, save_model
from src.exception import CustomException
from src.logger import get_logger

logger = get_logger(__name__)

def run_training_pipeline(uri, db_name, collection_name, model_path):
    try:
        # Data Ingestion
        logger.info("Starting data ingestion")
        df = ingest_data_from_mongodb(uri, db_name, collection_name)
        logger.info("Data ingestion completed successfully")

        # Data Transformation
        logger.info("Starting data transformation")
        X_train, X_test, y_train, y_test = transform_data(df)
        logger.info("Data transformation completed successfully")

        # Model Training
        logger.info("Starting model training")
        model = train_model(X_train, y_train)
        logger.info("Model training completed successfully")

        # Model Evaluation
        logger.info("Starting model evaluation")
        accuracy, report = evaluate_model(model, X_test, y_test)
        logger.info(f"Model evaluation completed successfully\nAccuracy: {accuracy}\nReport:\n{report}")

        # Save Model
        logger.info("Saving the model")
        save_model(model, model_path)
        logger.info(f"Model saved successfully at {model_path}")

    except CustomException as e:
        logger.error(f"An error occurred in the training pipeline: {e}")

if __name__ == "__main__":
    try:
        # Define MongoDB connection details
        uri = "mongodb://localhost:27017/"
        db_name = "your_database"
        collection_name = "your_collection"
        model_path = "models/random_forest_model.joblib"

        # Run the training pipeline
        run_training_pipeline(uri, db_name, collection_name, model_path)
    
    except CustomException as e:
        logger.error(f"An error occurred: {e}")