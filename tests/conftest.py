from datetime import datetime

import pytest
from py._xmlgen import html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.teller_config import BROWSER_NAME, CHROME_DRIVER_PATH, DOWNLOAD_FILE_DIRECTORY
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
        chrome_options = Options()
        # 不显示浏览器
        # chrome_options.add_argument('--headless')
        # 文件下载设置
        prefs = {
            "download.prompt_for_download": False,
            'download.default_directory': DOWNLOAD_FILE_DIRECTORY,  # 下载目录
            "plugins.always_open_pdf_externally": True,
            'profile.default_content_settings.popups': 0,  # 设置为0，禁止弹出窗口
            # 'profile.default_content_setting_values.images': 2,#禁止图片加载
        }
        chrome_options.add_experimental_option('prefs', prefs)
        logger.info('open browser ...')
        driver = webdriver.Chrome(options=chrome_options, executable_path=CHROME_DRIVER_PATH)
        driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior',
                  'params': {'behavior': 'allow', 'downloadPath': DOWNLOAD_FILE_DIRECTORY}}
        command_result = driver.execute("send_command", params)
        logger.info("response from browser:")
        for key in command_result:
            logger.info("result:" + key + ":" + str(command_result[key]))
    # driver.implicitly_wait(1)
    yield driver
    driver.quit()
    logger.info('link end ...')
