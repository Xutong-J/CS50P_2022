from numb3rs import validate
import pytest
import re

def test_non_num():
    assert validate("cat") == False
    assert validate("CAT.cat.0.0") == False
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False

def test_big():
    assert validate("512.512.512.512") == False
    assert validate("255.255.255.255") == True

def test_neg():
    assert validate("-10.1.-5.1") == False

def test_right():
    assert validate("0.0.0.0") ==True
    assert validate("192.168.1.1")==True
    assert validate(" 255.255.255.255 ") == True
    assert validate(" 255.255 .255.255 ") == False

def test_other_split():
    assert validate("192,168,1,1")==False
    assert validate("192 168 1 1")==False
    assert validate("192-168-1-1")==False
