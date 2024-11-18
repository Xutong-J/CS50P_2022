import pytest
from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("good morning") == "gd mrnng"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("GOOD MORNING") == "GD MRNNG"
