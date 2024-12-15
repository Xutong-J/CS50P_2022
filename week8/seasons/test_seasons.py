from seasons import get_birth, calculate
from datetime import date
import pytest

assert get_birth("2024-12-14") == date(2024, 12, 14)
with pytest.raises(SystemExit)
