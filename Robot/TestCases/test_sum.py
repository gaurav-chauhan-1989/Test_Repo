import pytest
from Pages import sum_calc
from Logging.test_logs import Test_Logs


class Testsum():
    '''def test_sum(self):
        a = sum_calc.sum_calc(1,2)
        assert a ==2'''

    def test_sum_with_monkeypatch(self, monkeypatch):                      # Using monkeypatch as fixture
        def mock_delay():                                                  # Creating a mock method
            print("No Delay using monkeypatch")

        monkeypatch.setattr("Pages.sum_calc.delay", mock_delay)            # Patching mock method in place of delay method
        a = sum_calc.sum_calc(1,2)
        assert a ==3
        self.logger = Test_Logs.custom_logs()
        self.logger.info("This is test log")

