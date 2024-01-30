import os 
import sys
from src.exception import Custom_exception
from src.logger import logging
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass  # used for making class variables 

#DataIngestionConfig: 
#This is a data class that defines paths for storing different types of data files 
# (train_data_path, test_data_path, raw_data_path). 
# These paths point to CSV files in an 'artifacts' directory. 
# The use of os.path.join ensures that the file paths are constructed correctly regardless of the operating system.
@dataclass 
class DataIngestionConfig:
    train_data_path : str=os.path.join('artifacts' ,"train.csv")
    test_data_path:str=os.path.join('artifacts' ,"test.csv")
    raw_data_path:str=os.path.join('artifacts' ,"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

## if data is stroed in some database i will write a code below to read that data afrom a database 
    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion method or compomnent")
        try:
            df = pd.read_csv('notebook\Data\stud.csv')  # initially just trying to run for csv and later we will learn how to read from anywhere 
            logging.info('Read the dataset as dataframe')


            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,  index=False, header=True )

            logging.info("Train test split initiated")

            train_set , test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,  index=False, header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,  index=False, header=True)

            logging.info("Ingestion of data is completed")

            return(
                self.ingestion_config.train_data_path, 
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise Custom_exception(e,sys)
        

if __name__== "__main__":
    obj= DataIngestion()
    obj.initiate_data_ingestion()


            


# This class handles the actual data ingestion process.

# In the initiate_data_ingestion method, it first logs the start of the data ingestion process.
# It tries to read a CSV file into a DataFrame (df). This CSV file is currently hardcoded as 'notebook\Data\stud.csv', which you mentioned would later be modified to read from a database.
# The method then ensures that the directory for the raw data file exists (using os.makedirs) and writes the DataFrame to this raw data path.
# It performs a train-test split on the DataFrame and saves the resulting training and testing sets to their respective paths defined in DataIngestionConfig.
# The method logs the completion of these steps and returns the paths to the train and test datasets.
# 