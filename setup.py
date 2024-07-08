from setuptools import find_packages, setup

setup(
    name='breast_cancer_ml_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'Flask'
    ]
)