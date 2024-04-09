import warnings

warnings.filterwarnings("ignore")
from us_visa.pipeline.train_pipeline import TrainPipeline

pipline  = TrainPipeline()
pipline.run_pipeline()
