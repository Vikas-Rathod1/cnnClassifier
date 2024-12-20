from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTraining_pipeline
from cnnClassifier import logger
##from pipeline.stage_01_data_ingestion import DataIngestionTraining_pipeline


STAGE_NAME =    "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>>>>>STAGE {STAGE_NAME} is started >>>>>>>>>>")

    data_ingestion  = DataIngestionTraining_pipeline()
    data_ingestion.main()

    logger.info(">>>>>>>>>>>>>STAGE {STAGE_NAME} is Completed >>>>>>>>>")
except Exception as e:
    #logger.info(f">>>>>>>>>>>>>STAGE {STAGE_NAME} is failed >>>>>>>>>")
    logger.exception(e)
    raise e