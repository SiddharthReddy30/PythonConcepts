import pytest
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