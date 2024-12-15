from seasons import get_birth, calculate
from datetime import date
import pytest
from inflect import engine

def test_get_birth():
    assert get_birth("2024-12-14") == date(2024, 12, 14)

    with pytest.raises(SystemExit):
        get_birth("20241214")
    with pytest.raises(SystemExit):
        get_birth("2024,12,14")
    with pytest.raises(SystemExit):
        get_birth("2024 12 14")

def test_calculate()
    p = engine()
    assert calculate(date(2024,12,14),date(2024,12,15)) == f"{p.number_to_words(1440, andword="")} minutes"
    assert calculate(date(2023,12,14),date(2024,12,15)) == "Five hundred twenty-seven thousand forty minutes"
    assert calculate(date(2023,12,14),date(2022,12,15)) == "Five hundred twenty-five thousand, six hundred minutes"
