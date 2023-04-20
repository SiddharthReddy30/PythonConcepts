import pytest

# To run specific tests, in a file
#   1.Substring matching
#     pytest -k <sub-string>
#   2.Set markers
#     pytest -m <marker-name>

#Xfail/skip
#Xfail - executes test but doesn't care about the output
#skip - skips the execution of the test.
@pytest.mark.xfail
@pytest.mark.greater
def test_greater():
    num = 100
    assert num > 100

@pytest.mark.skip
@pytest.mark.greater
def test_greater_equal():
    num = 100
    assert num >= 100

def test_less():
    num = 100
    assert num < 200
