from app.calc import mean, total


def test_mean():
    assert mean([1, 2, 3]) == 2.0
    assert mean([]) == 0.0


def test_total():
    assert total([1, 2, 3]) == 6
    assert total([]) == 0
