import pytest
import mod

@pytest.mark.integer
def test_case3():
    a=10
    b=20
    assert a+b==20

def test_case4():
    print('This is case 4')

def test_case5():
    mod.mod()

@pytest.mark.string
def test_case_6():
    str="This is gaurav chauhan"
    assert "gaurav" in str

@pytest.mark.string
def test_case_7():
    str="chauhan"
    assert "shekhar"==str

@pytest.mark.skip(reason="This has to be skipped")
def test_case_8():
    print("Not executed")