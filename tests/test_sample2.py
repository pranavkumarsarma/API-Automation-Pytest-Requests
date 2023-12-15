# test_example.py

import pytest

def add_numbers(a, b):
    return a + b

def test_add_numbers():
    assert add_numbers(2, 3) == 5

def test_add_numbers_negative():
    assert add_numbers(-1, 1) == 0

def test_add_numbers_float():
    assert add_numbers(2.5, 3.5) == 6.0

def test_add_numbers_str():
    with pytest.raises(TypeError):
        add_numbers("2", 3)