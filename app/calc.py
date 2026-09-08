"""Small numeric helpers used by the fixture project."""


def mean(values):
    """Return the arithmetic mean of values, or 0.0 if empty."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def total(values):
    """Return the sum of values."""
    return sum(values)
