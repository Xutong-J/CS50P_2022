from working import convert
import pytest

def test_no_m():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_VE():
    with pytest.raises(ValueError):
        convert("9：60 AM to 5：60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
       convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM 5:00 PM")
    with pytest.raises(ValueError):
        convert("13: 60 AM to 5: 20 PM")
    with pytest.raises(ValueError):
        convert("5AM to 9PM")
    with pytest.raises(ValueError):
        convert("11:00 AM 5:20 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:60 PM")


def test_nomal():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

