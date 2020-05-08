#!/usr/bin/env python
# coding=utf-8
import pytest
import logging

from framework.logger import Logger
from page_object.page_pypi import PagePIPY

logger = Logger(logger='TestSample').getLog()


class TestSample:

    @pytest.fixture(autouse=True, scope='function')
    def set_up(self, driver):
        url = 'https://pypi.org/'
        driver.get(url)
        logger.info('goto url %s' % url)

    def test_1(self, driver):
        """
        1.基础方法封装(base_action.py)
        2.页面对象(page_object/)
        3.页面操作(test_*.py)

        :param driver:
        :return:
        """
        page_pypi = PagePIPY(driver)
        title = page_pypi.get_banner()
        print(title)
