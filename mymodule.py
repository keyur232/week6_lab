def safe_divide(a: float, b: float) -> float:
    """Divides a by b, returns inf if b == 0."""
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')


def string_category(s: str) -> str:
    """
    Classify string:
    - empty -> 'empty'
    - all digits -> 'numeric'
    - all letters -> 'alphabetic'
    - mix -> 'alphanumeric'
    """
    if not s:
        return "empty"
    elif s.isdigit():
        return "numeric"
    elif s.isalpha():
        return "alphabetic"
    else:
        return "alphanumeric"
