"""Small numeric helpers used by the fixture project."""


def mean(values):
    """Return the arithmetic mean of values.

    Returns 0.0 when the input list is empty.
    """
    if not values:
        return 0.0
    return sum(values) / len(values)


def total(values):
    """Return the sum of values."""
    return sum(values)


def first_over(values: list[float], threshold: float) -> float:
    """Return the first value in values that exceeds threshold."""
    candidates = [v for v in values if v > threshold]
    return candidates[0]
