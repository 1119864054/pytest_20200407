from datetime import datetime

import pytest
from py._xmlgen import html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.teller_config import BROWSER_NAME, CHROME_DRIVER_PATH
from framework.logger import Logger

logger = Logger(logger='INIT').getLog()

driver = None


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        xfail = hasattr(report, 'wasxfail')
        report.extra = extra
    report.description = str(item.function.__doc__)


def pytest_html_report_title(report):
    report.title = "CECECECECECECECECE"


def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop()


def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop()


def pytest_configure(config):
    config._metadata['自定义1'] = 'test'


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p("自定义2: test")])


@pytest.fixture(scope='module', autouse=False)
def driver():
    logger.info('link start ...')
    global driver
    if BROWSER_NAME.upper() == 'CHROME':
        # 无头
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        logger.info('open browser ...')
        driver = webdriver.Chrome(options=chrome_options, executable_path=CHROME_DRIVER_PATH)
    # driver.implicitly_wait(1)
    yield driver
    driver.quit()
    logger.info('link end ...')
