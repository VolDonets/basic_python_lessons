import logging
import logging.config

logging.config.fileConfig("logging.conf")
# logging.config.dictConfig()

logger = logging.getLogger("simpleExample")
logger.debug("This is a debug message")
