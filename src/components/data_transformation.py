import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from src.exception import CustomException
from src.logger import get_logger

logger = get_logger(__name__)

def transform_data(df, target_column='target'):
    try:
        logger.info("Starting feature engineering process")

        # Handle missing values (example: fill missing values with the mean)
        logger.info("Handling missing values")
        df.fillna(df.mean(), inplace=True)

        # Separate features and target
        X = df.drop(columns=[target_column])
        y = df[target_column]

        # Encode categorical variables if any (example: using LabelEncoder)
        # Assuming `y` is categorical
        logger.info("Encoding categorical variables")
        if y.dtype == 'object':
            le = LabelEncoder()
            y = le.fit_transform(y)

        # Feature Scaling
        logger.info("Scaling numerical features")
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Splitting the data into training and testing sets
        logger.info("Splitting the data into training and testing sets")
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

        logger.info("Feature engineering process completed successfully")
        return X_train, X_test, y_train, y_test

    except Exception as e:
        logger.error(f"Error in feature engineering: {e}")
        raise CustomException("Error in feature engineering", e)
