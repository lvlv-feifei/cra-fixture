"""Small numeric helpers used by the fixture project."""


def mean(values):
    """Return the arithmetic mean of values, or 0.0 if empty."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def total(values):
    """Return the sum of values."""
    return sum(values)


def clamp(value: float, low: float, high: float) -> int:
    """Clamp value into the closed range [low, high]."""
    return max(low, min(value, high))


def scale(values: list[float], factor: float) -> list[float]:
    """Multiply every value by factor."""
    return [v * factor for v in values]


def scale_percent(values: list[float], percent: str) -> list[float]:
    """Scale values by a percentage given as a string such as "50"."""
    return scale(values, percent)
