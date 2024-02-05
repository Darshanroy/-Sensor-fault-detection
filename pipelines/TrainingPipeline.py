from zenml.config import DockerSettings
from zenml.integrations.constants import MLFLOW
# from zenml.pipelines import pipeline
from zenml import pipeline
from steps.DataIngestion_step import ingest_data
import pandas as pd
from steps.ModelTraining_step import train_model
from steps.DataCleaning_step import clean_data
from steps.DataEvaluvation_step import evaluation


docker_settings = DockerSettings(required_integrations=[MLFLOW])


@pipeline(enable_cache=True)
def train_pipeline():
    """
    Args:
        ingest_data: DataClass
        clean_data: DataClass
        model_train: DataClass
        evaluation: DataClass
    Returns:
        mse: float
        rmse: float
    """
    df = ingest_data()
    x_train, x_test, y_train, y_test = clean_data(df)
    model = train_model(x_train, x_test, y_train, y_test)
    mse, rmse = evaluation(model, x_test, y_test)
