import pytest
from addition import add,sub


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),          # Positive numbers
        (-2, -3, -5),       # Negative numbers
        (-2, 3, 1),         # Mixed positive and negative
        (0, 5, 5),          # Zero
        (0, 0, 0),          # Both zero
        (2.5, 3.5, 6.0),    # Floating-point numbers
        (100, 200, 300),    # Large numbers
    ]
)

def test_add(a, b, expected):
    assert add(a, b) == expected



@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, -1),          # Positive numbers
        (-2, -3, 1),       # Negative numbers
        (-2, 3, -5),         # Mixed positive and negative
        (0, 5, -5),          # Zero
        (0, 0, 0),          # Both zero
        (2.5, 3.5, -1),    # Floating-point numbers
        (100, 200, -100),    # Large numbers
    ]
)

def test_add(a, b, expected):
    assert sub(a, b) == expected
