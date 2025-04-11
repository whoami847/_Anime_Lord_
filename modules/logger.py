import logging

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AnimeLordBot")

def log(message):
    logger.info(message)

def error_log(message):
    logger.error(message)

def debug_log(message):
    logger.debug(message)
