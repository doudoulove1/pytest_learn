import pytest


def test_a():
    print("这是---")


def test_b():
    print("这是777777777777")


def test_c():
    assert 1 == 2


@pytest.mark.parametrize("a", (1, 2, 3))
@pytest.mark.parametrize("b", (4, 5, 6))
def test_prams(a, b):
    print(f"a = {a},b = {b}")
