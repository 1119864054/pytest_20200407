from framework.logger import Logger
from util.object_map import get_element

logger = Logger(logger='BaseAction').getLog()


class BaseAction(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element_text(self, loc):
        loc_type = loc[0]
        loc_expression = loc[1]
        try:
            logger.info("get_element_text : %s => %s" % (loc_type, loc_expression))
            element = get_element(self.driver, loc_type, loc_expression)
            element_text = element.text
            logger.info("get_element_text : %s " % element_text)
            return element_text
        except Exception as e:
            logger.error("get_element_text : %s " % e)
            raise e
