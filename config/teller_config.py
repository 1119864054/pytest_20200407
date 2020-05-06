import os

BROWSER_NAME = 'IE'

# local path
LOCAL_PATH = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))

# 浏览器驱动
CHROME_DRIVER_PATH = LOCAL_PATH + '/tools/chromedriver.exe'

LOG_PATH = LOCAL_PATH + '/logs/'
