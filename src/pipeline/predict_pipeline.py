import joblib
import pandas as pd
from src.exception import CustomException
from src.logger import get_logger
from src.utils import create_directory

logger = get_logger(__name__)

def load_model(model_path):
    try:
        logger.info(f"Loading model from {model_path}")
        model = joblib.load(model_path)
        logger.info("Model loaded successfully")
        return model
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        raise CustomException("Error loading model", e)

def predict(model, data):
    try:
        logger.info("Making predictions")
        predictions = model.predict(data)
        logger.info("Predictions made successfully")
        return predictions
    except Exception as e:
        logger.error(f"Error making predictions: {e}")
        raise CustomException("Error making predictions", e)

if __name__ == "__main__":
    try:
        # Example data (replace with actual data)
        data = pd.DataFrame({
            'mean radius': [17.99, 20.57, 19.69],
            'mean texture': [10.38, 17.77, 21.25],
            'mean perimeter': [122.8, 132.9, 130.0],
            'mean area': [1001.0, 1326.0, 1203.0],
            'mean smoothness': [0.1184, 0.08474, 0.1096]
            # Add other features as needed
        })

        model_path = "models/random_forest_model.joblib"
        model = load_model(model_path)
        predictions = predict(model, data)
        print("Predictions:", predictions)

    except CustomException as e:
        logger.error(f"An error occurred: {e}")
