from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTraining_pipeline

##from pipeline.stage_01_data_ingestion import DataIngestionTraining_pipeline
from cnnClassifier.pipeline.stage_02_preparebased_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.state_03_Training_model import ModelTrainingPipeline
from cnnClassifier import logger

STAGE_NAME =    "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>>>>> {STAGE_NAME} is started >>>>>>>>>>")

    data_ingestion  = DataIngestionTraining_pipeline()
    data_ingestion.main()

    logger.info(f">>>>>>>>>>>>> {STAGE_NAME} is Completed >>>>>>>>>")
except Exception as e:
    #logger.info(f">>>>>>>>>>>>>STAGE {STAGE_NAME} is failed >>>>>>>>>")
    logger.exception(e)
    raise e


STAGE_NAME =    "Prepare Base Model"

try:
    logger.info(f">>>>>>>>>>>>> {STAGE_NAME} is started >>>>>>>>>>")

    prepare_base_model  = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()

    logger.info(f">>>>>>>>>>>>> {STAGE_NAME} is Completed >>>>>>>>>X")
except Exception as e:
    #logger.info(f">>>>>>>>>>>>>STAGE {STAGE_NAME} is failed >>>>>>>>>")
    logger.exception(e)
    raise e



STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
