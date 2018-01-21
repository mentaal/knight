import pytest
from node import Node
def pytest_addoption(parser):
    parser.addoption("--board_size", type=int, default=5, help="The size of the board")
    parser.addoption("--param", type=int, nargs=2, help="The movement size")

@pytest.fixture(scope='session')
def board_size(request):
    return request.config.getoption("--board_size")

@pytest.fixture(scope='session')
def param(request):
    return request.config.getoption("--param")

