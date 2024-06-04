from ddt import ddt, data, unpack, file_data
from TestCases.TestBase import Test_Base
from Pages.login import login_page
from Utility.python_utils import Utils
import unittest




@ddt
class TestLogin(Test_Base, unittest.TestCase):

    utils_method = Utils()


    @data(*utils_method.read_excel_data('E:\\Sheet\\sht.xlsx', 'Sheet'))
    @unpack
    #@file_data("../Config/datayml.yaml")
    def test_login(self, name, email, phone):
        self.login = login_page(self.driver)
        self.login.login_meth(name, email, phone)

