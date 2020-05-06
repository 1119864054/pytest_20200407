import logging
import logging.handlers
import time

from config.teller_config import LOG_PATH


class Logger(object):

    def __init__(self, logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        date = time.strftime('%Y%m%d', time.localtime((time.time())))

        log_name = LOG_PATH + date + '.log'

        fh = logging.handlers.RotatingFileHandler(log_name, maxBytes=1024 * 1024, backupCount=5, encoding='utf-8')
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s [%(levelname)8s] [%(name)s] (%(filename)s:%(lineno)s) %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getLog(self):
        return self.logger
