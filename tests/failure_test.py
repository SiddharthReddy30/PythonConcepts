import pytest
import math

#maxfail
#It stops execution of tests after it fails mentioned number of test fails.
#pytest --maxfail <num>

def test_sqrt_failure():
    num = 25
    assert math.sqrt(num) == 6
    
def test_square_failure():
    num = 25
    assert num * num == 25
    
def test_equality_failure():
    num = 25
    assert num ==20 