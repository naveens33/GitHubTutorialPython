import pytest

from pages.accountsummarypage import AccountSummaryPage
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from pages.logout import LogoutPage
from pages.paybillspage import PayBillsPage
from testdata.readdata import getdata
from ctreport_selenium.ctlistener import Test, Priority, Severity


class Test_AddNewPayee:
    test = None

    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, driver):
        home = HomePage(driver)
        home.click_signin_button()
        login = LoginPage(driver)
        login.do_login("username", "password")
        acc = AccountSummaryPage(driver)
        acc.click_pay_bills_link()
        yield
        logout = LogoutPage(driver)
        logout.do_logout()

    @pytest.fixture(autouse=True)
    def nav_to_anp(self, driver):
        self.paybills = PayBillsPage(driver)
        self.paybills.click_add_new_payee_link()

    @pytest.mark.parametrize("name,addrs,acc,details", getdata())
    def test_add_new_payee(self, name, addrs, acc, details):
        self.test = Test("Add New Payee " + name, description="Adding a new payee to Zero Bank site",
                         priority=Priority.MEDIUM)
        self.test.log("Navigated successfully for Add New Payee Page")
        self.paybills.do_addnewpayee(name, addrs, acc, details)
        self.test.log("Successfully added the new payee")

    def teardown_method(self, method):
        Test_AddNewPayee.test = self.test
