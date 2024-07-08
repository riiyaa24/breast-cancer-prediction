import os

project_structure = [
    "src",
    "src/components",
    "src/pipeline",
    "notebooks",
    "data",
    "logs"
]

for folder in project_structure:
    os.makedirs(folder, exist_ok=True)

files = [
    "src/__init__.py",
    "src/logger.py",
    "src/exception.py",
    "src/utils.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/pipeline/__init__.py",
    "src/pipeline/predict_pipeline.py",
    "src/pipeline/train_pipeline.py",
    "import_data.py",
    "setup.py",
    "requirements.txt",
    ".gitignore",
    "README.md",
    "LICENSE"
]

for file in files:
    with open(file, 'w') as f:
        pass