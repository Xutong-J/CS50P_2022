from plates import is_valid

def test_long():
    assert is_valid("AAAAA678") == False
    assert is_valid("W") == False
def test_starter():
    assert is_valid("W3ERD") == False
    assert is_valid("2ewrt") == False
def test_middle():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True
def test_other():
    assert is_valid(" sdf34")  == False
    assert is_valid("AAA2,2")  == False
    assert is_valid("")  == False
def test_alphab():
    assert is_valid("AASDER") == True
