from pathlib import Path

class Config:
  RANDOM_SEED = 27
  ROOT_PATH = Path("../")
  LOG_FILE = ROOT_PATH / "logs/casuality_modeling.log"
  DATA_PATH = ROOT_PATH / "data/"
  