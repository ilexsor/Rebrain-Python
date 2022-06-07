# logger module
import logging


def get_logger(name):
    logger = logging.getLogger(name)
    handler = logging.FileHandler(filename='log_file.log')
    handler.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%B %d %H:%M:%S'))
    logger.addHandler(handler)

    return logger
