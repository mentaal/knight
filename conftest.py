def pytest_addoption(parser):
    parser.addoption("--board_size", type=int, default=5, help="The size of the board")
