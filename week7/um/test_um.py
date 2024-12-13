from um import count

def test_sign():
    assert count("um？") == 1
    assert count("Um, thanks, um...") == 2

def test_num():
    assert count("Um, thanks, um...") == 2
    assert count("hello, um, world") == 2
def test_um_words():
    assert count("yummy") == 0
