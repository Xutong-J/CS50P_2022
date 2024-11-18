from bank import value

def test_hello():
    assert value("hello") == '$0'
    assert value("Hello, James") == '$0'


def test_h():
    assert value("how are you?") == '$20'
    assert value("How do you do") == '$20'

def test_other():
    assert value("What do you do") == '$100'
    assert value("Good morning") == '$100'
