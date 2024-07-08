from flask import Flask, request, jsonify
from src.components.data_ingestion import ingest_data
from src.components.data_transformation import transform_data
from src.components.model_trainer import train_model, evaluate_model
import pandas as pd

app = Flask(__name__)

@app.route('/train', methods=['POST'])
def train():
    try:
        df = ingest_data("data/breast_cancer.csv")
        X_train, X_test, y_train, y_test = transform_data(df)
        model = train_model(X_train, y_train)
        accuracy = evaluate_model(model, X_test, y_test)
        return jsonify({"accuracy": accuracy})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)