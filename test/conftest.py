import os
import pytest

from functools import wraps


def file_io(func):
    @wraps(func)
    def wrapper(dic):
        f = open(dic, 'r')
        r = func(f)
        f.close()
        return r
    return wrapper


def file_index(ext):
    if ext == 'dic':
        return [os.path.join('src', 'en_US-web.dic')]
    return [os.path.join('src', 'en_US-web.aff')]


@pytest.fixture(params=file_index(ext='dic'))
def dic(request):
    return request.param


@pytest.fixture(params=file_index(ext='aff'))
def aff(request):
    return request.param
