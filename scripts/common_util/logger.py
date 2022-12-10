import logging
import sys
from scripts.common_util.constants import *
logger = logging.getLogger()

# specify here to change log level
log_level = logging.INFO
logger.setLevel(log_level)

file = 'logs/repo_search_auto' + str(time.time()) + '.log'

file_handler = logging.FileHandler(file)
handler = logging.StreamHandler(sys.stdout)

handler.setLevel(log_level)
file_handler.setLevel(log_level)

formatter = logging.Formatter("%(asctime)s - %(filename)s - %(message)s")

handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(file_handler)