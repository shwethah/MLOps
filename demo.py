import warnings
import time
warnings.filterwarnings("ignore")
from us_visa.pipeline.train_pipeline import TrainPipeline

start = time.time()
pipline  = TrainPipeline()
pipline.run_pipeline()
end  = time.time()
print(f"Total time taken: {end - start} seconds")
