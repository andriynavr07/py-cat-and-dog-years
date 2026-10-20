from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_below_first_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_first_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_second_human_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_older_ages() -> None:

    assert get_human_age(28, 29) == [3, 3]

    assert get_human_age(56, 64) == [10, 10]
