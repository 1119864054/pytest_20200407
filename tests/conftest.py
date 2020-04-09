from datetime import datetime

import pytest
from py._xmlgen import html
from pytest_html import extras


def pytest_html_report_title(report):
    report.title = "My very own title!"


def pytest_configure(config):
    config._metadata['foo'] = 'bar'


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p("foo: bar")])


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url('http://www.baidu.com/'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML MYMYMY</div>'))
        report.extra = extra
    extra.append(pytest_html.extras.text('some string', name='Different title'))


def test_extra(extra):
    extra.append(extras.text('some string'))


def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop()


def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop()
