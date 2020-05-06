from selenium.webdriver.support.ui import WebDriverWait

# 单个
def get_element(driver, loc_type, loc_expression):
    try:
        element = WebDriverWait(driver, 10).until(
            lambda x: x.find_element(by=loc_type, value=loc_expression)
        )
        return element
    except Exception as e:
        raise e

# 多个
def get_elements(driver, loc_type, loc_expression):
    try:
        elements = WebDriverWait(driver, 10).until(
            lambda x: x.find_elements(by=loc_type, value=loc_expression)
        )
        return elements
    except Exception as e:
        raise e
