# Breast Cancer Prediction Project

This project demonstrates a machine learning pipeline for predicting breast cancer using the `load_breast_cancer` dataset from `sklearn.datasets`. The project includes data ingestion, data transformation, model training, and model prediction.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

1. Clone the repository:

    ```sh
    git clone
    cd repo-name
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up the MongoDB database and collection:

    - Ensure MongoDB is running.
    - Use the provided `src/import_data.py` script to load the dataset into MongoDB.

## Usage

### Training the Model

To run the training pipeline:

```sh
python src/pipeline/train_pipeline.py

### Making Predictions
To make predictions using the trained model:

sh
python src/pipeline/predict_pipeline.py


### Project Structure 
├── src
│   ├── __init__.py
│   ├── components
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   ├── pipeline
│   │   ├── __init__.py
│   │   ├── predict_pipeline.py
│   │   ├── train_pipeline.py
│   ├── utils.py
│   ├── logger.py
│   ├── exception.py
├── models
│   └── random_forest_model.joblib
├── logs
│   └── <log-files>.log
├── import_data.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
