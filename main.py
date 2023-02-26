from test import get_requirements
from sensor.exception import SensorException
from sensor.logger import logging
import sys,os
from sensor.constant.env_variable import MONGODB_URL_KEY
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainPipeline


if __name__=="__main__":
    try:
        pipeline = TrainPipeline()
        data_ingestion_artifact = pipeline.run_pipeline()
        print(data_ingestion_artifact)
        # print(os.getenv(MONGODB_URL_KEY))
    except Exception as e:
        raise SensorException(e, sys)