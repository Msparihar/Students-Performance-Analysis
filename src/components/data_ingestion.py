import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts','train_data.csv')
    test_data_path = os.path.join('artifacts','test_data.csv')
    raw_data_path = os.path.join('artifacts','raw_data.csv')
    
class DataIngestion:
    def __init__(self):
        self.IngestionConfig = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging("Entered data ingestion.")
        try:
            # Read the dataset
            df = pd.read_csv("notebook/data/stud.csv")
            logging("Sucessfully read the dataset.")
            
            os.makedirs(os.path.dirname(self.IngestionConfig.train_data_path), exist_ok=True)
            
            df.to_csv(self.IngestionConfig.raw_data_path, index=False, header=True)
            
            logging("Initialized train test split.")
            train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)
            
            train_data.to_csv(self.IngestionConfig.train_data_path, index=False, header=True)
            test_data.to_csv(self.IngestionConfig.test_data_path, index=False, header=True)
            
            logging("Ingestion completed successfully.")
            
            return(
                self.IngestionConfig.train_data_path,
                self.IngestionConfig.test_data_path
            )
            
            
        except:
            raise CustomException(e,sys)
