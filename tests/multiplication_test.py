import pytest

#Test result in XML format
#pytest <test-file> -v --junitxml=result.xml 
@pytest.mark.parametrize('num, output',
                         [(1,11),
                          (2,22),
                          (3,33)])
def test_multiplication(num, output):
    assert 11*num == output
