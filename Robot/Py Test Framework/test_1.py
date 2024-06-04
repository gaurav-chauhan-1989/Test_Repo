import pytest

class Test_1():

    @pytest.hookimpl
    def pytest_runtest_setup(self, item):
        print("This is setup hook")

    @pytest.hookimpl
    def pytest_runtest_teardown(self, item):
        print("This is teardown hook")

    @pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (4, 5, 8), (3, 4, 7)])
    def test_case1(self, a, b, expected):
        c = a+b
        assert c==expected
        #self.soft_assert(self.assertEqual, c, expected)
        #self.assert_all()


    @pytest.mark.smoke
    def test_case2(self):
        print('This is case 2')

