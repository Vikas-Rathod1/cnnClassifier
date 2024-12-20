from cnnClassifier.config import configuration
from cnnClassifier.components import DataIngestion
from cnnClassifier import logger



class Training_pipeline:
    def __init__():
        pass

    def main():


        # Example usage
        try:
            config = configuration.ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            
            # Download the zip file
            data_ingestion.download_file()
            
            # Unzip and clean the files
            data_ingestion.unzip_and_clean()
        except Exception as e:
            print(f"An error occurred: {e}")