import pytest

@pytest.mark.dependency()
@pytest.mark.parametrize("a,b,result", [(1,2,3), (2,3,5)])
def test_validate_data(a,b,result):
    assert result == a+b

@pytest.mark.dependency(depens=["test_validate_data"])
def test_2():
    print("Hello")
