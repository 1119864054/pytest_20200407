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
        driver.get('https://pypi.org/')

    def test_1(self, driver):
        page_pypi = PagePIPY(driver)
        title = page_pypi.get_banner()
        print(title)
