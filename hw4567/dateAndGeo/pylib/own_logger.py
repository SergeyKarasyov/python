import logging
import logging.config
import os
# 3 module: write your own logger which can be used in module1/module2 and show logs in console and pass it to log file in parallel.
# Moreover it report dateime, filename, process and pid / class|function,
# log priority (DEBUG...INFO) for each log message.


def get_logger(name):
    LOGFILE = os.environ.get('LOGFILE', '/tmp/{}.log'.format(name))
    logger = logging.getLogger(name)
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(LOGFILE, encoding='utf8')
    formatter = logging .Formatter(
        '[%(asctime)s][%(processName)s %(process)-6d] [%(module)s ] [%(filename)s %(lineno)d] [%(funcName)-20s] [%(levelname)-8s] [delay %(relativeCreated)d] %(message)s')
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger


logger = get_logger('hw4')
