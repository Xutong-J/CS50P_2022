import pytest
from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("good morning") == "gd mrnng"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("GOOD MORNING") == "GD MRNNG"

def test_numb():
    assert shorten("FAIzAN1") == "FzN1"
    assert shorten("3tEST") == "3tST"

def test_punc():
    assert shorten(".FAIzAN1") == ".FzN1"
    assert shorten("1.twitter") == "1.twttr"
