from fuel import convert, gauge

def test_cnvrt():
    assert convert('3/4') == 75
    assert convert('1/4') == 25
    assert convert('4/4') == 100
    assert convert('0/4') == 0
