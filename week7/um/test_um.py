from um import count
import pytest

def test_sign():
    assert count("um？") == 1
    assert count("Um, thanks, um...") == 2

def test_num():
    assert count("Um, thanks, um...") == 2
    assert count("hello, um, world") == 1

def test_um_words():
    assert count("yummy") == 0
    assert count("circumference") == 0
