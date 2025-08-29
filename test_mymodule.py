import pytest
from mymodule import safe_divide, string_category

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 2, 3.0),
        (5, 0, float('inf')),
        (-10, -2, 5.0),
    ]
)
def test_safe_divide(a, b, expected):
    assert safe_divide(a, b) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("", "empty"),
        ("12345", "numeric"),
        ("hello", "alphabetic"),
        ("abc123", "alphanumeric"),
    ]
)
def test_string_category(text, expected):
    assert string_category(text) == expected
