import pytest
import math
import pytestSample as ps

@pytest.mark.parametrize(
    ('input', 'expected'),
    (
        (5,25),
        (3., 9.),
    )
)

def test_square(input, expected):
    assert ps.sqare(input) == expected
    
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5 