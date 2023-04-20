import pytest

#fixtures are functions, which run before the tests and feed them their output as input
#generally its use to feed database connections, URLs etc

@pytest.fixture
def inputValue():
    value =39
    return value

def test_div_by_3(inputValue):
    assert inputValue % 3 == 0 

def test_div_by_6(inputValue):
    assert inputValue % 6 == 0 