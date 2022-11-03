import sys
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.constant import training_pipeline
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.pipeline.training_pipline import TrainPipeline


'''def test_exception():
    try:
        logging.info('we are deviding 1 by zero')  #this is add in logger 
        x=1/0
    except Exception as e:
        raise SensorException(e,sys)


if __name__=='__main__':


   try:
        test_exception()
   except Exception as e:
        print(e)'''


# mongodb_client=MongoDBClient()
# #  print('collection_name:', mongodb_client.database.list_collection_names())

'''if __name__=='__main__':
    training_pipeline_config=TrainingPipelineConfig()
    data_ingetion_config=DataIngestionConfig(training_pipeline_config=training_pipeline_config)
    print(data_ingetion_config.__dict__)'''

if __name__=='__main__':
    training_pipeline=TrainPipeline()
    training_pipeline.run_pipeline()









#Output Exception: Error occurred python script name [main.py] line number [7] error message [division by zero]
