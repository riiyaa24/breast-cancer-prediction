from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
from src.exception import CustomException
from src.logger import get_logger

logger = get_logger(__name__)

def train_model(X_train, y_train):
    try:
        logger.info("Starting model training")

        # Initialize and train the model
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)

        logger.info("Model training completed successfully")
        return model
    except Exception as e:
        logger.error(f"Error in model training: {e}")
        raise CustomException("Error in model training", e)

def evaluate_model(model, X_test, y_test):
    try:
        logger.info("Starting model evaluation")

        # Make predictions
        predictions = model.predict(X_test)

        # Calculate accuracy
        accuracy = accuracy_score(y_test, predictions)

        # Generate classification report
        report = classification_report(y_test, predictions)

        logger.info("Model evaluation completed successfully")
        return accuracy, report
    except Exception as e:
        logger.error(f"Error in model evaluation: {e}")
        raise CustomException("Error in model evaluation", e)

def save_model(model, file_path):
    try:
        logger.info("Saving the trained model")
        joblib.dump(model, file_path)
        logger.info(f"Model saved successfully at {file_path}")
    except Exception as e:
        logger.error(f"Error in saving the model: {e}")
        raise CustomException("Error in saving the model", e)