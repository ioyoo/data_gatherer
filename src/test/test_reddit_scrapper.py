from ..reddit_scrapper import func


def test_func():
    assert func(1, 1, 1) == -1


def test_not_func():
    assert func(2, 2, 2) != 2
