from cnnClassifier.config import configuration
from cnnClassifier.components import PrepareBaseModel
from cnnClassifier import logger
from cnnClassifier.config import ConfigurationManager


class PrepareBaseModelTrainingPipeline:
    def __init__(self): # type: ignore
        pass

    def main(self): # type: ignore


        # Example usage
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            print(f"An error occurred: {e}")