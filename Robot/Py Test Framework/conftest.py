import pytest

@pytest.fixture()
def URL():
    print('Before Method')
    yield
    print('After Method')