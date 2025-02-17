from plates import is_valid

def test_long():
    assert is_valid("AAAAA678") == False
    assert is_valid("W") == False
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False
def test_starter():
    assert is_valid("W3ERD") == False
    assert is_valid("2ewrt") == False
def test_numeric():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True
def test_alphabetical():
    assert is_valid(" sdf34")  == False
    assert is_valid("AAA2,2")  == False
    assert is_valid("")  == False
    assert is_valid("ABCDEF")  == True
def test_zero():
    assert is_valid("AAA54") == True
    assert is_valid("AAA05") == False
cd
