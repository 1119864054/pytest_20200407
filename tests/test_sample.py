#!/usr/bin/env python
# coding=utf-8
import pytest
import logging

logger = logging.getLogger('TestAnser')

def inc(x):
    return x + 1


def test_answer():
    logger.info('lohlohlhlhohlh')
    assert inc(3) == 5


if __name__ == "__main__":
    pytest.main(['-sv', "C:\\Users\\11198\\PycharmProjects\\pytest_20200407", "--html", "report.html"])
