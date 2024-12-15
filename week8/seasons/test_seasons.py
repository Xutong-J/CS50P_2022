from seasons import get_birth, calculate
from datetime import date
import pytest


def test_get_birth():
    assert get_birth("2024-12-14") == date(2024, 12, 14)

    with pytest.raises(SystemExit):
        get_birth("20241214")
    with pytest.raises(SystemExit):
        get_birth("2024,12,14")
    with pytest.raises(SystemExit):
        get_birth("2024 12 14")

def test_calculate():

    assert calculate(date(2024,12,14),date(2024,12,15)) == "One thousand, four hundred forty minutes"
    assert calculate(date(2023,12,15),date(2024,12,15)) == "Five hundred twenty-seven thousand forty minutes"

