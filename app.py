import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from logger import logging # type: ignore
from exception import CustomException # type: ignore
from src.components.data_ingestion import DataIngestion
from src.components.data_ingestion import DataIngestionConfig



if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)
