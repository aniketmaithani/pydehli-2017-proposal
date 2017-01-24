from .sample_python_program import (addition, subtraction, increment_by_one)


def test_addition():
    assert addition(3, 5) == 8
    assert addition(5, 4) == 9

def test_subtraction():
    assert subtraction(5, 4) == 1

def test_increment_by_one():
    assert increment_by_one(4) == 5
