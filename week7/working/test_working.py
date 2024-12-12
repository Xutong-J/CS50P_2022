from working import convert
import pytest

def test_no_m():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10：30 PM to 8 AM") == "22:30 to 08:00"

def test_VE():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
