import pytest

#fixtures are functions, which run before the tests and feed them their output as input
#generally its use to feed database connections, URLs etc
@pytest.fixture
def inputValue():
    value =39
    return value